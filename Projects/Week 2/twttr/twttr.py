def slang_text():
    user_input = input('Input: ')
    vowels = 'aeiouAEIOU'
    for i in vowels:
        if i in user_input:
            user_input = user_input.replace(i, '')
    print('Output:', user_input)

slang_text()
