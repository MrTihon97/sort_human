def import_data(data, sep=None):
    with open('text.txt', 'a+', encoding='utf-8') as file:
        if sep == None:
            file.write(f"\n")
            for i in data:
                file.write(f"/n")
            file.write(f"/n")
        else:
            file.write(f"\n")
            file.write(sep.join(data))
            file.write(f"")
