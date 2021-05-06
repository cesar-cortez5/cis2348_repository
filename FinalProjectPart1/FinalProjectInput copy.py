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
            if i[5] == "damaged":
                damaged_list.append(i)

        item_in_inv = False
        # Finished checking for manufacturer and item type. Need to add to check for different item types/manufactures in one string (lenovo apple computer, dell phone laptop,)
        for i in full_inventory_list:
            other_items = []
            manufacturer = i[1].lower()
            item_type = i[2].lower()
            item_id = i[0]

            if (manufacturer in query) and (item_type in query) and (item_id != j[0]) and (i not in damaged_list):

                customer_manufacturer = manufacturer
                customer_item_type = item_type
                customer_id = item_id
                customer_price = i[3]
                item_in_inv = True

        if item_in_inv:
            print(
                f"Your item is: {customer_id}, {customer_manufacturer}, {customer_item_type}, {customer_price}")
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
        Item1.customer_query(query)
