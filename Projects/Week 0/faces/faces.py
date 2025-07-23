def convert(user_input):
    text = user_input.replace(':)', '🙂')
    text = text.replace(':(', '🙁')

    return text

def main():
    user_input = input()
    output = convert(user_input)
    print(output)
    return output

main()
