#Cesar Cortez
#PSID = 1836168
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    heart_rate = (220 - 35) * 0.7
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        bpm = fat_burning_heart_rate(age)
        print(f"Fat burning heart rate for a {age} year-old: {bpm} bpm")

    except ValueError:
        print("Invalid age.\nCould not calculate heart rate info.")