def main():
    greet = input('Greeting: ').lower()
    output = greeting(greet)
    print(output)

def greeting(greet):
    if 'hello' in greet.lower():
        return '$0'
    elif greet[0].lower() == 'h':
        return '$20'
    else:
        return '$100'

if __name__ == "__main__":
    main()