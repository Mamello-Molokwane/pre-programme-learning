months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

# Make sure input is in correct format, Month-Day-Year so either 9/8/1636 or September 8, 1636
# If not correct format ask for input again
# Then output in the format: YYYY-MM-DD


def date(months_dictionary):
    while True:
        user_input = input('Date: ')
        # Checking if user_input is in correct format and handling result
        if '/' in user_input:
            month, day, year = user_input.split('/')
            try:
                int(month)
            except ValueError:
                continue
        elif ' ' in user_input and ',' in user_input:
            user_input = user_input.replace(',', '')
            month, day, year = user_input.split(' ')
        else:
            continue

        # turning month, day and year into integers
        try:
            month, day, year = int(month), int(day), int(year)
            if month > 12:
                continue
        except ValueError:
            try:
                day, year = int(day), int(year)
                # Getting month string into correct month number according to months_dictionary
                month = month.title()
                for i in months_dictionary:
                    if i == month:
                        month = months_dictionary[i]
            except ValueError:
                continue
        if day > 31:
            continue
        # Turning it into correct format
        print('{:4d}-{:02d}-{:02d}'.format(year, month, day))
        break


date(months)