def exact_change(user_total):
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

    new_total = user_total

    while new_total != 0:
        while new_total > 99:
            num_dollars += 1
            new_total -= 100

        while new_total > 24:
            num_quarters += 1
            new_total -= 25

        while new_total > 9:
            num_dimes += 1
            new_total -= 10

        while new_total > 4:
            num_nickels += 1
            new_total -= 5

        while new_total > 0:
            num_pennies += 1
            new_total -= 1

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__':
    user_total = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(user_total)

    if user_total == 0:
        print("no change")

    if num_dollars > 1:
        print(str(num_dollars) + " dollars")
    if num_dollars == 1:
        print(str(num_dollars) + " dollar")

    if num_quarters > 1:
        print(str(num_quarters) + " quarters")
    if num_quarters == 1:
        print(str(num_quarters) + " quarter")

    if num_dimes > 1:
        print(str(num_dimes) + " dimes")
    if num_dimes == 1:
        print(str(num_dimes) + " dime")

    if num_nickels > 1:
        print(str(num_nickels) + " nickels")
    if num_nickels == 1:
        print(str(num_nickels) + " nickel")

    if num_pennies > 1:
        print(str(num_pennies) + " pennies")
    if num_pennies == 1:
        print(str(num_pennies) + " penny")


