print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

first_service = str(input("Select first service:\n"))
second_service = str(input("Select second service:\n\n"))

first_service_lower = first_service.lower()
second_service_lower = second_service.lower()

service_price = {"oil change": 35,
                "tire rotation": 19,
                "car wash": 7,
                "car wax": 12,
                 "-": "No service"}

first_service_price = service_price[first_service_lower]
second_service_price = service_price[second_service_lower]

if first_service == "-" or second_service == "-":
    if first_service == "-":
        total = second_service_price
        print(f"Davy's auto shop invoice\n\nService 1: {first_service_price}\nService 2: {second_service}, ${second_service_price}\n\nTotal: ${total}")
    elif second_service == "-":
        total = first_service_price
        print(f"Davy's auto shop invoice\n\nService 1: {first_service}, ${first_service_price}\nService 2: {second_service_price}\n\nTotal: ${total}")
else:
    total = first_service_price + second_service_price
    print(f"Davy's auto shop invoice\n\nService 1: {first_service}, ${first_service_price}\nService 2: {second_service}, ${second_service_price}\n\nTotal: ${total}")



