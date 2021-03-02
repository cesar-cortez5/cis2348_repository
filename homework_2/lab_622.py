#Cesar Cortez
#PSID = 1836168

counter = 1
number_list = []

while counter <= 6:
    number_input = int(input(""))
    number_list.append(number_input)
    counter += 1
x1_coef, y1_coef, number, x2_coef, y2_coef, number2 = number_list[0], number_list[1], number_list[2], number_list[3], number_list[4], number_list[5]

has_solution = False
for x in range(-10, 10):
    for y in range(-10, 10):
        if (x * x1_coef) + (y * y1_coef) == number:
            if (x * x2_coef) + (y * y2_coef) == number2:
                solution = f"{x} {y}"
                has_solution = True

if has_solution:
    print(solution)
else:
    print("No solution")
