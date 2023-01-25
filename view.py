
def choise():
    choise = int(input(
        '1 - добавить пользователя \n 2 - вывести таблицу \n 3 - вывести только имя и фамилию \n 4 - отсортировать по именам \n 5 - отсортировать по id\n 6 - выход\n'))
    return choise

def print_table():
    with open('human_list.txt','r', encoding= 'utf 8') as file:
        for line in file.readlines():
            print(line,end='')

def print_only_names():
    with open('human_list.txt','r', encoding= 'utf 8') as file:
        for line in file.readlines():
            temp = line.split(' ')
            print(f'Имя - {temp[1]} Фамилия - {temp[2]}')
