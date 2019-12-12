if __name__ == '__main__':
    data = ''
    with open('name.txt', 'w+') as file:
        while True:
            data = input('Podaj imię i nazwisko lub quit, aby wyjść: ')
            if 'quit' == data:
                break

            file.write(data.replace(' ', ', ') + '\n')

        file.seek(0) #cofamy kursor - żeby nie startowal od pustej linijki
        names = file.readlines()[::-1]
        for i in names:
            first_name, surname = i.split(',')
            print(f'{surname.strip}, {first_name}')