def main():
    user_input = input('What time is it? ')
    output = convert(user_input)
    if 8 >= output >= 7:
        print('breakfast time')
    elif 13 >= output >= 12:
        print('lunch time')
    elif 19 >= output >= 18:
        print('dinner time')

def convert(time):
    time = time.split(':')
    hours = float(time[0])
    minutes = float(time[1])/60
    output = hours + minutes
    return output


if __name__ == "__main__":
    main()
