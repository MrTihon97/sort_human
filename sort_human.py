def sort_names():
    with open('human_list.txt','r+', encoding= 'utf 8') as file:
        lst_with_str = file.readlines()
        lst_with_lst = []
        for line in lst_with_str:
            temp = line.split(' ')
            lst_with_lst.append(temp)
        lst_with_lst = sorted(lst_with_lst,key = lambda x:x[1])
        file.seek(0)
        for worker in lst_with_lst:
            file.write(' '.join(worker))
        print('Отсортировано!')
def sort_id():
    with open('human_list.txt','r+', encoding= 'utf 8') as file:
        lst_with_str = file.readlines()
        lst_with_lst = []
        for line in lst_with_str:
            temp = line.split(' ')
            lst_with_lst.append(temp)
        lst_with_lst = sorted(lst_with_lst,key = lambda x:x[0])
        file.seek(0)
        for worker in lst_with_lst:
            file.write(' '.join(worker))
        print('Отсортировано!')