#Cesar Cortez
#PSID = 1836168

import math

height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))

area = height * width
print(f"Wall area: {area} square feet")

paint_needed = area / 350
cans_needed = math.ceil(paint_needed)
print('Paint needed: {:.2f} gallons'.format(paint_needed))
print(f"Cans needed: {cans_needed} can(s)\n")

color = str(input("Choose a color to paint the wall:\n"))

color_prices = {"red": 35,
                "blue": 25,
                "green": 23}
price = color_prices[color] * cans_needed

print(f"Cost of purchasing {color} paint: ${price}")

