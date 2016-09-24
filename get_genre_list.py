def get_genre_list():

    def get_file_key():

        file_key = input("What kind of list do you want? Please input the associated number.\n"
                         "(1) Music\n"
                         "(2) Movies\n"
                         "(3) Games\n"
                         "(4) Restaurants\n"
                         "(5) Choose your own list\n")
        works = False
        while not works:
            try:
                assert(0 < int(file_key) <= 5)
                works = True
            except Exception:
                file_key = input("Please input a number from 1 to 5.\n")

        if file_key == '1':
            file_str = 'Music.txt'
            list_type = 'Music'
        elif file_key == '2':
            file_str = 'Movies.txt'
            list_type = 'Movies'
        elif file_key == '3':
            file_str = 'Games.txt'
            list_type = 'Games'
        elif file_key == '4':
            file_str = 'Restaurants.txt'
            list_type = 'Restaurants'
        elif file_key == '5':
            file_str = input("Please enter the file name of the list you want to use.\n")
            works = False
            while not works:
                try:
                    open(file_str, 'r')
                    works = True
                except Exception:
                    file_str = input("Please enter a valid file name.\n")
            list_type = 'Custom'
        return file_str, list_type

    file_str, list_type = get_file_key()
    file = open(file_str, 'r')
    genres = file.readline()
    genres = genres.split()
    file.readline()
    type_string = file.readline()
    genre_list = genres + [type_string] + [list_type]

    return genre_list

print(get_genre_list())
