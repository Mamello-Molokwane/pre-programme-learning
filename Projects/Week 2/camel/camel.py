def camel_to_snake():
    user_input = input('camelCase: ')
    for letter in user_input:
        if letter.isupper():
            user_input = user_input.replace(letter, f'_{letter.lower()}')
    print('snake_case:', user_input)

camel_to_snake()
