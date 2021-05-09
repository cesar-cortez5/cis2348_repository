# Cesar Cortez
#PSID - 1836168



import csv
from datetime import datetime

# Defining the class named Item


class Item:
    # Initializing the class with the attributes manufuctured, price, and service_date, which are all list
    def __init__(self, manufacturer, price, service_date):
        self.manufacturer = manufacturer
        self.price = price
        self.service_date = service_date

    def customer_query(self, query):
        full_inventory_list = []
        damaged_list = []
        for i in self.manufacturer:
            for j in self.price:
                for k in self.service_date:
                    if i[0] == k[0] and i[0] == k[0] and i[0] == j[0]:
                        full_inventory_list.append(
                            [i[0], i[1], i[2], j[1], k[1], i[3]])

        for i in full_inventory_list:
            date = i[4]
            date_string = datetime.strptime(date, "%m/%d/%Y")

            if i[5] == "damaged" or date_string.date() < datetime.now().date():
                damaged_list.append(i)

        item_in_inv = False
        # Finished checking for manufacturer and item type. Need to add to check for different item types/manufactures in one string (lenovo apple computer, dell phone laptop,)
        customer_items = []
        similar_items = []
        for i in full_inventory_list:
            manufacturer = i[1].lower()
            item_type = i[2].lower()
            item_id = i[0]

            if item_type in query and i not in damaged_list:
                similar_items.append([item_id, manufacturer, item_type, i[3]])

            if (item_type in query) and (i not in damaged_list) and (manufacturer in query):
                item_in_inv = True
                customer_items.append([item_id, manufacturer, item_type, i[3]])

            customer_items.sort(reverse=True, key=lambda x: x[3])
            similar_items.sort(reverse=True, key=lambda x: x[3])

        if item_in_inv:
            print(
                f"Your item is: {customer_items[0][0]}, {customer_items[0][1]}, {customer_items[0][2]}, {customer_items[0][3]}")
            if len(similar_items) > 1 and customer_items[0] != similar_items[0]:
                print(
                    f"You may, also, consider: {similar_items[0][0]}, {similar_items[0][1]}, {similar_items[0][2]}, {similar_items[0][3]}")
            elif len(similar_items) > 1 and customer_items[0] == similar_items[0]:
                print(
                    f"Your may, also, consider: {similar_items[1][0]}, {similar_items[1][1]}, {similar_items[1][2]}, {similar_items[1][3]}")

        else:
            print(f"No such item in inventory")


# Main function that opens each file, takes each row from each CSV file, and imports it to a list
def file_opener():
    manufacturer_list = []
    with open('ManufacturerList.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            manufacturer_list.append(row)

    price_list = []
    with open('PriceList.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            price_list.append(row)

    service_dates_list = []
    with open('ServiceDatesList.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            service_dates_list.append(row)

    return manufacturer_list, price_list, service_dates_list


# Main function
if __name__ == "__main__":

    manufacturer_list, price_list, service_dates_list = file_opener()
    # Creating an instance of an Item known as Item1
    Item1 = Item(manufacturer_list, price_list, service_dates_list)

    query = ""

    while query != "q":
        query = input("Please enter the item type and manufacturer\n")
        Item1.customer_query(query.lower())
