import json
import datetime


# Функция для добавления заметки
def add_note():
    id = input("Введите ID заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    # Читаем существующие заметки из файла
    with open("notes.json", "r") as file:
        notes = json.load(file)

    notes.append(note)

    # Сохраняем заметки в файл
    with open("notes.json", "w") as file:
        json.dump(notes, file)

    print("Заметка успешно добавлена.")


# Функция для чтения заметок
def read_notes():
    with open("notes.json", "r") as file:
        notes = json.load(file)

    for note in notes:
        print("ID:", note["id"])
        print("Заголовок:", note["title"])
        print("Текст:", note["body"])
        print("Время создания/изменения:", note["timestamp"])
        print()


# Функция для редактирования заметки
def edit_note():
    id = input("Введите ID заметки, которую хотите отредактировать: ")

    with open("notes.json", "r") as file:
        notes = json.load(file)

    note_found = False
    for note in notes:
        if note["id"] == id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            note_found = True

    if note_found:
        with open("notes.json", "w") as file:
            json.dump(notes, file)
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка с указанным ID не найдена.")


# Функция для удаления заметки
def delete_note():
    id = input("Введите ID заметки, которую хотите удалить: ")

    with open("notes.json", "r") as file:
        notes = json.load(file)

    note_found = False
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            note_found = True

    if note_found:
        with open("notes.json", "w") as file:
            json.dump(notes, file)
        print("Заметка успешно удалена.")
    else:
        print("Заметка с указанным ID не найдена.")


# Основной цикл программы
while True:
    print("1. Добавить заметку")
    print("2. Показать заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Введите номер команды: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Неверная команда. Попробуйте еще раз.")