#Cesar Cortez
#PSID = 1836168
number_list = input().split()
new_list = []

for number in number_list:
    number = int(number)
    if number >= 0:
        new_list.append(number)

new_list.sort()
for number in new_list:
    print(number, end=' ')
