def add_human():
    id = int(input('Введите id человека: '))
    name = input('Введите имя человека: ')
    lastname = input('Введите фамилию человека: ')
    number = int(input('Введите номер телефона человека: '))
    comments = input('Введите коментарий: ')
    line = f'{id} {name} {lastname} {number} {comments}\n'
    with open('human_list.txt','a', encoding= 'utf 8') as file:
        file.write(line)
    print('сохранено')