password_weak = input("\n")
password = ""
characters = {"i": "!",
              "a": "@",
              "m": "M",
              "B": "8",
              "o": "."}

for character in password_weak:
    if character in characters.keys():
        password = password + characters[character]
    else:
        password = password + character

password = password + "q*s"

print(password)



