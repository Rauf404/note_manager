# Создаем список хранящий информацию о заметке

note = [ ]

# Запрос информации от пользователя

user_name = input('Введите имя пользоваеля: ')
title1 = input('Введите первый заголовок заметки: ')
title2 = input('Введите второй заголовок заметки: ')
title3 = input('Введите третий заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки ( например: "Активно", "Готово","Планирую начать")')
created_date = input('Введите дату создания заметки в формате ДД-ММ-ГГГГ: ')
issue_date = input('Введите дату дедлайна в формате ДД-ММ-ГГГГ: ')

# Создаем список для заголовков

titles = [title1, title2, title3]

# Добавляем в список все собранные данные

note.append(user_name)
note.append(titles)
note.append(content)
note.append(status)
note.append(created_date)
note.append(issue_date)

# Вывод собранных данных через список

print(note)