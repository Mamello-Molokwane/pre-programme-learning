def gauge():
    result = True
    while result:
        num = input('Fraction: ')
        try:
            first, sec = num.split('/')
            if int(first) < 0 or int(sec) < 0:
                raise ValueError
            elif isinstance(first, float) or isinstance(sec, float):
                raise ValueError
            elif int(first) > int(sec):
                raise ValueError
            num = int(first) / int(sec)
            dec = num * 100
            dec = round(dec)
            if int(dec) <= 1:
                dec = 'E'
                break
            elif int(dec) >= 99:
                dec = 'F'
                break
            result = False
            break
        except (ZeroDivisionError, ValueError) as error:
            continue
    if isinstance(dec, int):
        print(f'{dec}%')
    else:
        print(dec)

gauge()
