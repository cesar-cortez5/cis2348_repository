parts = input().split()
name, age = parts[0], parts[1]

while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError:
        age = 0
        print('{} {}'.format(name, age))

    parts = input().split()
    name = parts[0]