menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def order(menu):
    cash = 0
    while True:
        try:
            user_input = input('Item: ').title()
        except EOFError:
            if cash > 0:
                print('\nThank you for buying.')
            break
        for i in menu:
            if user_input == i:
                cash += menu[i]
                print(f'Total: ${cash:.2f}')
        continue
    print(f'Total: ${cash:.2f}')


order(menu)
