def shopping():
    grocery_list = {}
    while True:
        try:
            key = input().upper()
        except EOFError:
            print('\n')
            break
        if key in grocery_list:
            grocery_list[key] += 1
        else:
            grocery_list[key] = 1
    if grocery_list:
        sorted_grocery_list = sorted(grocery_list.items())
        dict_grocery_list = dict(sorted_grocery_list)
        for i in dict_grocery_list:
            print(f'{dict_grocery_list[i]} {i}')

shopping()
