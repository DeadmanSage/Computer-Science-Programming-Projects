import csv
import os

# Inventory = r'C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Inventory.csv'
Inventory = r'Program\Inventory.csv'
with open(Inventory) as Equipment:
    InventoryReader = csv.reader(Equipment)
    InventoryArray = list(InventoryReader)
    print(InventoryArray)

attributes = ['Type','Name','Job','UC','Available']

temp = []
dropdown = []

for item in InventoryArray:
    Category = dict(zip(attributes, item))

with open(Inventory) as readObj:
    # pass the file object to reader() to get the reader object
    csvReader = csv.reader(readObj)
    next(csvReader)
    # Iterate over each row in the csv using reader object
    for row in csvReader:
        x = dict(zip(attributes, row))
        temp.append(x)
        

print(temp)


    






Users = r'C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Users.csv'
with open(Users) as People:
    UsersReader = csv.reader(People)
    UserArray = list(UsersReader)
# print(UserArray)


