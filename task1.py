def leap_year(x):
    if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
        return True
    else:
        return False


while True:
    try:
        year = int(input("Please enter year: "))
        if year <= 0:
            print("Value has to be more then zero!")
            continue
        else:
            print(leap_year(year))
            break
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
