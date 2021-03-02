#Cesar Cortez
#PSID = 1836168

import csv
name = str(input())
number_of_word = {}
with open(name, 'r') as inputfile:
    reader = csv.reader(inputfile)
    for i in reader:
        for word in i:
            if word not in number_of_word.keys():
                number_of_word[word] = 1
            else:
                number_of_word[word] += 1

for i in number_of_word.keys():
    print(f"{i} {str(number_of_word[i])}")

