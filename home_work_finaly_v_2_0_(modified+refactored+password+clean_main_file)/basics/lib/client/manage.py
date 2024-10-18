def manage_tasks_and_achievements(app):
    def save_ach_and_tasks():
        # Сохранение задач
        with open('task_list.txt', 'w', encoding='utf8') as file:
            file.write(app.get_tasks())

        # Сохранение ачивок
        with open('achievements_list.txt', 'w', encoding='utf8') as file:
            for achievement in app.get_achievements():
                file.write(
                    f'Ачивка: "{achievement.name}"\nДата получения: {achievement.receipt_date}; \nУсловия выдачи: "{achievement.description}";\n\n')

    def read_ach_and_tasks():
        # Чтение задач
        try:
            with open('task_list.txt', 'r', encoding='utf8') as file:
                print('Ваши задачи:')
                print(file.read())
        except FileNotFoundError:
            print("Файл задач не найден.")

        # Чтение ачивок
        try:
            with open('achievements_list.txt', 'r', encoding='utf8') as file:
                print("\nСписок ачивок:")
                print(file.read().strip())
        except FileNotFoundError:
            print("Файл ачивок не найден.")

    save_ach_and_tasks()
    read_ach_and_tasks()