#Cesar Cortez
#PSID - 1836168


import csv
from datetime import datetime

#Defining the class named Item
class Item:
    #Initializing the class with the attributes manufuctured, price, and service_date, which are all list 
    def __init__(self, manufacturer, price, service_date):
        self.manufacturer = manufacturer
        self.price = price
        self.service_date = service_date

    def full_inventory(self):
        #Defining an empty list
        row_list = []
        #Indexing through each list to retrive the ID, manufucurer, item type, price, service date, and if it's damaged
        for i in self.manufacturer:
            for j in self.price:
                for k in self.service_date:
                    #Checking for ID's from each list and if it's the same
                    if i[0] == k[0] and i[0] == k[0] and i[0] == j[0]:
                        #Making a list of the elements and appending it to row_list
                        row_list.append([i[0], i[1], i[2], j[1], k[1], i[3]])
                        #Sorting alphabetically by manufacturer
                        row_list.sort(key=lambda x: x[1])  
                        #Writing into the file "FullInventory.csv"
                        with open('FullInventory.csv', 'w', newline='') as file:
                            for l in row_list:
                                writer = csv.writer(file)
                                writer.writerow(l)


    def item_type_inventory(self):
        row_list = []
        for i in self.manufacturer:
            for j in self.price:
                for k in self.service_date:
                    if i[0] == k[0] and i[0] == k[0] and i[0] == j[0]:
                        row_list.append([i[0], i[1], i[2], j[1], k[1], i[3]])
                        #Sorting the list using the item's ID, which is located at index 0
                        row_list.sort(key=lambda x: x[0])  
                        #Iterating through each item list within the whole row_list in order to create a new file for each type of item
                        for item in row_list:
                            item_type = item[2]
                            #Capitalizing the item type for formatting. Eg. LaptopInventory.csv instead of laptopInventory.csv
                            item_type_name = item_type.capitalize()
                            with open(f'{item_type_name}Inventory.csv', 'w', newline='') as file:
                                for l in row_list:
                                    #Checking if the item type within the list already exists as a file. If it doesn't it creates a new file and if it does it just appends do it.
                                    if l[2] == item_type:
                                        writer = csv.writer(file)
                                        writer.writerow(l)       
                                    else:
                                        continue        



    def past_service(self):
        row_list = []
        for i in self.manufacturer:
            for j in self.price:
                for k in self.service_date:
                    service_date = k[1]
                    #Iterating through each list within the service date list, and then formatting the date 
                    service_date_string = datetime.strptime(service_date, "%m/%d/%Y")
                    if i[0] == k[0] and i[0] == k[0] and i[0] == j[0]:  
                        #Checking if date is past due or not   
                        if service_date_string.date() < datetime.now().date():                            
                            row_list.append([i[0], i[1], i[2], j[1], k[1], i[3]])
                            #Sorting the list by the date 
                            row_list.sort(key=lambda date: datetime.strptime(date[4], "%m/%d/%Y"))
                            with open('PastServiceDateInventory.csv', 'w', newline='') as file:
                                for l in row_list:
                                    writer = csv.writer(file)
                                    writer.writerow(l)

    def damaged_inventory(self):
        row_list = []
        for i in self.manufacturer:
            for j in self.price:
                for k in self.service_date:
                    if i[0] == k[0] and i[0] == k[0] and i[0] == j[0]:
                        row_list.append([i[0], i[1], i[2], j[1], k[1], i[3]])
                        #Sorting list by price
                        row_list.sort(reverse=True, key=lambda x: x[3])  
                        with open('DamagedInventory.csv', 'w', newline='') as file:
                            for l in row_list:
                                #Checking if item is damaged. If it is it writes to the file and if is not it skips the iteration.
                                if l[5] == "damaged":
                                    writer = csv.writer(file)
                                    writer.writerow(l)
                                else:
                                    continue

    def customer_query(self, query):
        print(query)

        pass


    

#Main function that opens each file, takes each row from each CSV file, and imports it to a list
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




#Main function
if __name__ == "__main__":



    manufacturer_list, price_list, service_dates_list = file_opener()
    #Creating an instance of an Item known as Item1
    Item1 = Item(manufacturer_list, price_list, service_dates_list)

    query = input("Please enter the item type and manufacturer\n")
    Item1.customer_query(query)

    '''
    Item1.full_inventory()
    Item1.past_service()
    Item1.damaged_inventory()
    Item1.item_type_inventory()
    '''







                        
                    




