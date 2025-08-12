def main():
    word = input('Input: ')
    print('Output:', shorten(word))

def shorten(user_input):
    vowels = 'aeiouAEIOU'
    for i in vowels:
        if i in user_input:
            user_input = user_input.replace(i, '')
    return user_input

if __name__ == "__main__":
    main()
