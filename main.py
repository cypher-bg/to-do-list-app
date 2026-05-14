from todo_module import TasksManager


def print_menu():
    # Показва основното меню на програмата

    print("\n========== TO-DO LIST APPLICATION ==========")
    print("1. Добави нова задача")
    print("2. Покажи всички задачи")
    print("3. Маркирай задача като изпълнена")
    print("4. Изтрий задача")
    print("5. Търси задача")
    print("6. Покажи изпълнени задачи")
    print("7. Покажи неизпълнени задачи")
    print("8. Сортирай по приоритет")
    print("9. Сортирай по краен срок")
    print("10. Редактирай задача")
    print("11. Покажи статистика")
    print("0. Изход")
    print("===========================================")


def read_task_number():
    # Чете номер на задача и обработва грешки

    try:
        task_number = int(input("Въведете номер на задача: "))
        return task_number

    except ValueError:
        print("Моля, въведете валидно число.")
        return None


def main():
    # Създаваме обект от класа TaskManager
    manager = TasksManager()

    while True:
        print_menu()

        choice = input("Изберете опция: ")

        if choice == "1":
            title = input("Име на задачата: ")
            description = input("Описание: ")
            priority = input("Приоритет /нисък, среден, висок/: ").lower()
            due_date = input("Краен срок /ден-месец-година/: ")

            manager.add_task(title, description, priority, due_date)

        elif choice == "2":
            manager.show_all_tasks()

        elif choice == "3":
            manager.show_all_tasks()
            task_number = read_task_number()

            if task_number is not None:
                manager.complete_task(task_number)

        elif choice == "4":
            manager.show_all_tasks()
            task_number = read_task_number()

            if task_number is not None:
                manager.delete_task(task_number)

        elif choice == "5":
            keyword = input("Въведете ключова дума за търсене: ")
            manager.search_task(keyword)

        elif choice == "6":
            manager.show_completed_tasks()

        elif choice == "7":
            manager.show_uncompleted_tasks()

        elif choice == "8":
            manager.sort_by_priority()
            manager.show_all_tasks()

        elif choice == "9":
            manager.sort_by_due_date()
            manager.show_all_tasks()

        elif choice == "10":
            manager.show_all_tasks()
            task_number = read_task_number()

            if task_number is not None:
                new_title = input("Ново име на задачата: ")
                new_description = input("Ново описание: ")
                new_priority = input("Нов приоритет /нисък, среден, висок/: ").lower()
                new_due_date = input("Нов краен срок /ден-месец-година/: ")

                manager.edit_task(
                    task_number,
                    new_title,
                    new_description,
                    new_priority,
                    new_due_date
                )

        elif choice == "11":
            manager.show_statistics()

        elif choice == "0":
            print("Изход от програмата. Довиждане!")
            break

        else:
            print("Невалидна опция. Моля, опитайте отново.")


if __name__ == "__main__":
    main()