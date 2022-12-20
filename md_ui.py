import md_controller

def start():
    str = "\nЭто база данных сотрудников.\nОна использует внутреннюю БД в формате json, файл по умолчанию contacts_DB.json.\nОсновные функции:\n\
    \t- добавлять, удалять и редактировать контакты;\n \
    \t- экспортировать данные в форматах .txt и .csv;\n \
    \t- импортировать данные в форматах .txt и .csv;\n \
    \t- осуществлять поиск сотрудников по:\n \
    \t\t - имени и фамилии;\n \
    \t\t - должности;\n \
    \t\t - зарплате, необходимо указать нижнюю и верхнюю границы."
        
    print(f'\033[32m{str}\033[30m\n')
    

def menu():
    menu = []
    menu.append("\nМеню:")
    menu.append(' 1 - Создать новую книгу или очистить существующую')
    menu.append(' 2 - Добавить новый контакт')
    menu.append(' 3 - Удалить контакт')
    menu.append(' 4 - Редактировать контакт')
    menu.append(' 5 - Найти контакт')
    menu.append(' 6 - Показать все контакты')
    menu.append(' 7 - Экспортировать контакты в файл .txt')
    menu.append(' 8 - Экспортировать контакты в файл .csv')
    menu.append(' 9 - Импортировать контакты из файла .txt')
    menu.append('10 - Импортировать контакты из файла .csv')
    menu.append('11 - Выход')
    
    print(*menu, sep = '\n')
    return md_controller.inputProcessing()

def menu_search():
    menu = []
    menu.append(' 1 - По имени или фамилии')
    menu.append(' 2 - По должности')
    menu.append(' 3 - По зарплате')   
     
    print(*menu, sep = '\n')
    return md_controller.inputProcessing()
