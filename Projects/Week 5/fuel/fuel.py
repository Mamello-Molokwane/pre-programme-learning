def main():
    while True:
        try:
            num = input('Fraction: ')
            whole_num = convert(num)
            output = gauge(whole_num)
            break
        except (TypeError, ZeroDivisionError, ValueError):
             continue
    print(output)



def convert(num):
    first, sec = num.split('/')
    if int(first) < 0 or int(sec) < 0:
        raise ValueError
    elif isinstance(first, float) or isinstance(sec, float):
        raise ValueError
    elif int(sec) == 0:
         raise ZeroDivisionError
    elif int(first) > int(sec):
        raise ValueError
    num = int(first) / int(sec)
    dec = num * 100
    dec = round(dec)
    print('convert:', dec)
    return dec

def gauge(percentage):
    if percentage <= 1:
                return 'E'
    elif percentage >= 99:
        return'F'
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()

# testing = input('Fraction: ')
# convert(testing)
