import Note

#создание заметки
def create_note(min_size):
    name = check_len_text(input('Напишите название заметки: '), min_size)
    content = input('Напишите содержание заметки: ')
    return Note.Note(name=name, content=content)

#проверка заметки
def check_len_text(text, min_size):
    while len(text) <= min_size:
        print(f'Текст не должен быть меньше {min_size} символов')
        text = input('\n Введите текст: \n')
    else:
        return text
