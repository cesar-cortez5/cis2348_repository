#Cesar Cortez
#PSID = 1836168


def prompt():
    age = 0
    happy_birthday = False
    print("Birthday Calculator\nCurrent Day")
    current_month = int(input("Month: "))
    current_day = int(input("Day: "))
    current_year = int(input("Year: "))
    print("Birthday")
    birth_month = int(input("Month: "))
    birth_day = int(input("Day: "))
    birth_year = int(input("Year: "))

    if current_month < birth_month:
        age = current_year - birth_year - 1
    elif birth_month == current_month:
        if current_day < birth_day:
            age = current_year - birth_year - 1
        elif birth_day == current_day:
            age = current_year - birth_year
            happy_birthday = True
        else:
            age = current_year - birth_year
    elif current_month > birth_month:
        age = current_year - birth_year

    print(f"You are {age} years old.")

    if happy_birthday:
        print("Happy Birthday!")




if __name__ == '__main__':
    prompt()

