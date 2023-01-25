import view as v
import sort_human as simh
import import_human as imh

def start():
    while True:
        choise = v.choise()
        if choise == 1:
            imh.add_human()
        elif choise == 2:
            v.print_table()
        elif choise == 3:
            v.print_only_names()
        elif choise == 4:
            simh.sort_names()
        elif choise == 5:
            simh.sort_id()
        elif choise == 6:
            break