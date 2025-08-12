from emoji import emojize

def text_to_emoji():
    user_input = input('Input: ')
    print('Output:', emojize(user_input, language='alias'))

text_to_emoji()
