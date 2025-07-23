def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    change_to = d.replace('$', '')
    return float(change_to)


def percent_to_float(p):
    to_float = p.replace('%', '')
    calc = float(to_float) / 100
    return calc


main()