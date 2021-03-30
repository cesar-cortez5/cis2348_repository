#Cesar Cortez
#PSID - 1836168

team = {}

i = 1
counter = 1

for i in range (1, 6):
    jersey = int(input(f"Enter player {i}'s jersey number:\n"))
    rating = int(input(f"Enter player {i}'s rating:\n\n"))

    if jersey < 0 and jersey > 99 and rating < 0 and rating > 9:
        print("Invalid entry")
        break
    else:
        team[jersey] = rating

print("ROSTER")
for jersey, rating in sorted(team.items()):
    print(f"Jersey number: {jersey}, Rating: {rating}")

menu_option = ""

while menu_option.upper() != "Q":
    print(f"\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")

    menu_option = input('Choose an option:\n')

    if menu_option == 'a':
        jersey = int(input('Enter a new player\'s jersey number:\n'))
        rating = int(input('Enter the players\'s rating:\n'))
        team[jersey] = rating

    elif menu_option == 'd':
        jersey = int(input('Enter a jersey number:\n'))
        if jersey in team.keys():
            del team[jersey]

    elif menu_option == 'u':
        jersey = int(input('Enter a jersey number:\n'))
        if jersey in team.keys():
            rating = int(input('Enter a new rating for player:\n'))
            team[jersey] = rating


    elif menu_option == 'r':
        rating_input=int(input('Enter a rating:\n'))
        print(f"ABOVE {rating_input}")
        for jersey,rating in sorted(team.items()):
            if rating > rating_input:
                print(f"Jersey number: {jersey}, Rating: {rating}")

    elif menu_option == 'o':
        print("ROSTER")


        for jersey,rating in sorted(team.items()):
            print(f"Jersey number: {jersey}, Rating: {rating}")

    
