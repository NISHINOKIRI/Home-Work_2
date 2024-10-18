def num_done_tasks(app, num_tasks):
    while True:
        u_input =(
            input
            ("\nПометить какие-то задачи как решённые?"
            "\nЕсли ДА, введите их ID через пробел\n"
            "Если НЕТ, просто нажмите' + ' ENTER ' + 'для выхода \n"))
        try:
            ids_to_remove = list(map(int, u_input.split()))  # Преобразуем ввод в список ID
            for task_id in ids_to_remove:
                if task_id < 1 or task_id > num_tasks:
                    print(f"ID {task_id} вне диапазона задач. Введите ID от 1 до {num_tasks}.")
                    break
                app.remove_task(task_id)  # Удаление задачи по ID
            else:
                break  # Выход из цикла, если все ID корректны
        except ValueError:
            print('Введите корректные ID задач через пробел или просто нажмите' + ' ENTER ' + 'для выхода \n')


# def num_done_tasks_old(app, num_tasks):
#     while True:
#         u_input = input("\nПометить какие-то задачи как решённые?\nЕсли да, введите число, если нет, введите 'нет'\n")
#         if u_input.lower()  == "нет":  # Проверка на "нет"
#             return
#         try:
#             num_tasks_to_remove = int(u_input)
#             if num_tasks_to_remove < 1:
#                 print("Введите число больше 0")
#                 continue
#             if num_tasks_to_remove > num_tasks:
#                 print(f"Введите число не больше {num_tasks}.")
#                 continue
#             for i in range(num_tasks_to_remove):
#                 app.remove_task(i + 1)  # Задачи нумеруются с 1
#             break  # Выход из цикла
#         except ValueError:
#             print('Введите число (int) \n')