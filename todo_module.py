import json
from datetime import datetime


class TasksManager:
    def __init__(self, filename="tasks.json"):
        # Име на файла, в който ще се пазят задачите
        self.filename = filename

        # Списък, който ще съдържа всички задачи
        self.tasks = []

        # При стартиране опитваме да заредим задачите от файла
        self.load_tasks()

    def load_tasks(self):
        # Зарежда задачите от JSON файл
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.tasks = json.load(file)

        except FileNotFoundError:
            # Ако файлът не съществува, започваме с празен списък
            self.tasks = []

        except json.JSONDecodeError:
            # Ако файлът е празен или повреден
            print("Файлът със задачи е повреден. Започва се с празен списък.")
            self.tasks = []

    def save_tasks(self):
        # Записва всички задачи във файл
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=4)

        except Exception as error:
            print(f"Грешка при запис във файл: {error}")

    def validate_date(self, date_text):
        # Проверява дали датата е във формат ГГГГ-ММ-ДД
        try:
            datetime.strptime(date_text, "%d-%m-%Y")
            return True
        except ValueError:
            return False

    def add_task(self, title, description, priority, due_date):
        # Добавя нова задача

        if title.strip() == "":
            print("Името на задачата не може да бъде празно.")
            return

        if priority not in ["нисък", "среден", "висок"]:
            print("Приоритетът трябва да бъде един от: нисък, среден или висок.")
            return

        if not self.validate_date(due_date):
            print("Невалиден формат на дата. Използвайте ГГГГ-ММ-ДД.")
            return

        task = {
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        }

        self.tasks.append(task)
        self.save_tasks()

        print("Задачата е добавена успешно.")

    def show_all_tasks(self):
        # Показва всички задачи

        if len(self.tasks) == 0:
            print("Няма добавени задачи.")
            return

        print("\n--- Всички задачи ---")

        for index, task in enumerate(self.tasks, start=1):
            self.print_task(index, task)

    def print_task(self, index, task):
        # Помощен метод за красиво извеждане на една задача

        status = "Изпълнена" if task["completed"] else "Неизпълнена"

        print(f"\nЗадача №{index}")
        print(f"Име: {task['title']}")
        print(f"Описание: {task['description']}")
        print(f"Приоритет: {task['priority']}")
        print(f"Краен срок: {task['due_date']}")
        print(f"Статус: {status}")

    def complete_task(self, task_number):
        # Маркира задача като изпълнена

        try:
            if task_number < 1 or task_number > len(self.tasks):
                print("Невалиден номер на задача.")
                return

            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()

            print("Задачата е маркирана като изпълнена.")

        except Exception as error:
            print(f"Възникна грешка: {error}")

    def delete_task(self, task_number):
        # Изтрива задача

        try:
            if task_number < 1 or task_number > len(self.tasks):
                print("Невалиден номер на задача.")
                return

            deleted_task = self.tasks.pop(task_number - 1)
            self.save_tasks()

            print(f"Задачата '{deleted_task['title']}' беше изтрита.")

        except Exception as error:
            print(f"Възникна грешка: {error}")

    def search_task(self, keyword):
        # Търси задачи по ключова дума

        found_tasks = []

        for task in self.tasks:
            if keyword.lower() in task["title"].lower() or keyword.lower() in task["description"].lower():
                found_tasks.append(task)

        if len(found_tasks) == 0:
            print("Няма намерени задачи.")
            return

        print("\n--- Намерени задачи ---")

        for index, task in enumerate(found_tasks, start=1):
            self.print_task(index, task)

    def show_completed_tasks(self):
        # Показва само изпълнените задачи

        completed_tasks = []

        for task in self.tasks:
            if task["completed"]:
                completed_tasks.append(task)

        if len(completed_tasks) == 0:
            print("Няма изпълнени задачи.")
            return

        print("\n--- Изпълнени задачи ---")

        for index, task in enumerate(completed_tasks, start=1):
            self.print_task(index, task)

    def show_uncompleted_tasks(self):
        # Показва само неизпълнените задачи

        uncompleted_tasks = []

        for task in self.tasks:
            if not task["completed"]:
                uncompleted_tasks.append(task)

        if len(uncompleted_tasks) == 0:
            print("Няма неизпълнени задачи.")
            return

        print("\n--- Неизпълнени задачи ---")

        for index, task in enumerate(uncompleted_tasks, start=1):
            self.print_task(index, task)

    def sort_by_priority(self):
        # Сортира задачите по приоритет

        priority_order = {
            "висок": 1,
            "среден": 2,
            "нискък": 3
        }

        self.tasks.sort(key=lambda task: priority_order[task["priority"]])
        self.save_tasks()

        print("Задачите са сортирани по приоритет.")

    def sort_by_due_date(self):
        # Сортира задачите по краен срок

        self.tasks.sort(key=lambda task: task["due_date"])
        self.save_tasks()

        print("Задачите са сортирани по краен срок.")

    def edit_task(self, task_number, new_title, new_description, new_priority, new_due_date):
        # Редактира съществуваща задача

        if task_number < 1 or task_number > len(self.tasks):
            print("Невалиден номер на задача.")
            return

        if new_title.strip() == "":
            print("Името на задачата не може да бъде празно.")
            return

        if new_priority not in ["нисък", "среден", "висок"]:
            print("Приоритетът трябва да бъде един от: нисък, среден или висок.")
            return

        if not self.validate_date(new_due_date):
            print("Невалиден формат на дата.")
            return

        self.tasks[task_number - 1]["title"] = new_title
        self.tasks[task_number - 1]["description"] = new_description
        self.tasks[task_number - 1]["priority"] = new_priority
        self.tasks[task_number - 1]["due_date"] = new_due_date

        self.save_tasks()

        print("Задачата е редактирана успешно.")

    def show_statistics(self):
        # Показва статистика за задачите

        total = len(self.tasks)
        completed = 0
        uncompleted = 0

        for task in self.tasks:
            if task["completed"]:
                completed += 1
            else:
                uncompleted += 1

        print("\n--- Статистика ---")
        print(f"Общо задачи: {total}")
        print(f"Изпълнени задачи: {completed}")
        print(f"Неизпълнени задачи: {uncompleted}")