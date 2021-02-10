lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))

servings = float(input("How many servings does this make?\n"))


print('\nLemonade ingredients - yields {0:.2f} servings\n{1:.2f} cup(s) lemon juice\n{2:.2f} cup(s) water\n{3:.2f} cup(s) agave nectar\n'.format(servings, lemon_juice, water, agave_nectar))

servings_desired = float(input("How many servings would you like to make?\n"))

lemon_juice_desired = servings_desired / (servings/lemon_juice)
water_desired = servings_desired / (servings/water)
agave_nectar_desired = servings_desired / (servings/agave_nectar)

print('\nLemonade ingredients - yields {0:.2f} servings\n{1:.2f} cup(s) lemon juice\n{2:.2f} cup(s) water\n{3:.2f} cup(s) agave nectar\n'.format(servings_desired, lemon_juice_desired, water_desired, agave_nectar_desired))

lemon_juice_gallons = lemon_juice_desired / 16
water_gallons = water_desired / 16
agave_nectar_gallons = agave_nectar_desired / 16

print('Lemonade ingredients - yields {0:.2f} servings\n{1:.2f} gallon(s) lemon juice\n{2:.2f} gallon(s) water\n{3:.2f} gallon(s) agave nectar'.format(servings_desired, lemon_juice_gallons, water_gallons, agave_nectar_gallons))