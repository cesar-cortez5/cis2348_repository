#Cesar Cortez
#PSID = 1836168

phrase = input()
phrase_stripped = phrase.strip().lower().replace(" ", "")
phrase_reversed = phrase[::-1].replace(" ", "")

if phrase_stripped == phrase_reversed:
    print(f"{phrase} is a palindrome")
else:
    print(f"{phrase} is not a palindrome")
