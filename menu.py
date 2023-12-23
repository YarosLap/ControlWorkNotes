import operation
import ui

#создание операций
def run():
    command = ''
    while command != '7':
        ui.menu()
        command = input().strip()
        if command == '1':
            operation.show('all')
        elif command == '2':
            operation.add()
        elif command == '3':
            operation.show('id')
            operation.id_delete()
        elif command == '4':
            operation.show('id')
            operation.id_rewrite()
        elif command == '5':
            operation.show('date')
            operation.date_show()
        elif command == '6':
            operation.show('id')
            operation.id_show()
        elif command == '7':
            bye()
            break
        else:
            print('Вы не ввели корректный номер команды')

#точка выхода
def bye():
    print('Выполнение программы завершено. Спасибо за использование и хорошего дня!')