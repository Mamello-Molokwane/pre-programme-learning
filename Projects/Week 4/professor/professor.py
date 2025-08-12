import random

def main():
    level = get_level()
    count = 0
    num = 0
    track = 0

    while track < 9:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = int(input(f'{x} + {y} = '))
        equation = x + y
        if answer == equation:
            num+=1
            count = 0
        else:
            while answer != equation:
                count+=1
                if count == 3:
                    print('Answer', equation)
                    break
                else:
                    print('EEE')
                #print(f'count: {count}')
                    answer = int(input(f'{x} + {y} = '))

            if answer == equation:
                num+=1
        track+=1

    print(f'Score: {num}')

def get_level():
    while True:
        try:
            user_input = int(input('level: '))
            if user_input > 3 or user_input < 1:
                continue
            else:
                return user_input
        except ValueError:
            continue


def generate_integer(level):
    if 1 > level > 3:
        raise ValueError
    elif level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x= random.randint(10, 99)
    else:
        x = random.randint(100, 999)

    return x

if __name__ == "__main__":
     main()