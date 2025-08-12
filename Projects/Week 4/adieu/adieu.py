import inflect

def song_greet():
    p = inflect.engine()
    names = []
    while True:
        try:
            user_input = input('Name: ')
            names.append(user_input)
        except EOFError:
            print('\n')
            break
    print('Adieu, adieu, to', p.join(names))


song_greet()
