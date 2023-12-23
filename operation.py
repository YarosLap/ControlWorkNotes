import file_handler
import Note
import note_builder

min_size = 3

#метод добавления заметки
def add():
    note = note_builder.create_note(min_size)
    array = file_handler.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_handler.write_file(array, 'a')
    print('Заметка добавлена')

#метод для вывода заметок
def show(text):
    logic = True
    array = file_handler.read_file()
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.info(notes))

        elif text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes) + '; Название: ' + Note.Note.get_name(notes) + '.')

        elif text == 'date':
            logic = False
            print('Дата создания: ' + Note.Note.get_date(notes) + '; Название: ' + Note.Note.get_name(notes) + '.')

    if logic == True:
        print('Сохраните новую заметку')

#метод перезаписи заметок
def id_rewrite():
    id = input(
        'Выберете ID  заметки, которую хотите перезаписать: ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            note = note_builder.create_note(min_size)
            Note.Note.set_name(notes, note.get_name())
            Note.Note.set_content(notes, note.get_content())
            Note.Note.set_date(notes)
            print('Изменения сохранены')
    if logic == True:
        print('Указанная заметка не найдена. Проверьте ID')
    file_handler.write_file(array, 'a')

#метод удаления заметок
def id_delete():
    id = input('Введите ID заметки, которую хотите удалить: ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            prov = input('Подтвердите удаление заметки (y или n): ').strip().lower()
            if prov == 'y':
                array.remove(notes)
                print('Заметка удалена')
            elif prov == 'n':
                print('Операция удаления заметки отменена')
    if logic == True:
        print('Указанная заметка не найдена. Проверьте ID')
    file_handler.write_file(array, 'a')

#метод отображения заметок по ID
def id_show():
    id = input('Введите ID заметки: ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            print(Note.Note.info(notes))
    if logic == True:
        print('Заметка не найдена. Проверьте ID')
    file_handler.write_file(array, 'a')

#метод отображения заметок по дате и времени
def date_show():
    date = input('Введите дату и время последнего редактирования: ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if date == Note.Note.get_date(notes):
            logic = False
            print(Note.Note.info(notes))
    if logic == True:
        print('Заметка не найдена. Проверьте ID')
    file_handler.write_file(array, 'a')
