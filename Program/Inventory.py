import csv

#Inventory = r'C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Inventory .csv'
Inventory = r"C:\Users\Biowa\Desktop\Computer-Science-Programming-Projects\Program\Login.txt"
with open(Inventory) as Equipment:
    InventoryReader = csv.reader(Equipment)
    InventoryArray = list(InventoryReader)
# print(InventoryArray)

attributes = ['Type','Name','Job','UC','Available']
temp = []

with open('Inventory.csv', 'r') as readObj:
    # pass the file object to reader() to get the reader object
    csvReader = csv.reader(readObj)
    # Iterate over each row in the csv using reader object
    for row in csvReader:
        x = dict(zip(attributes, row))
        temp.append(x)
       
print(temp)

for item in InventoryArray:
    test = dict(zip(attributes, item))

print(test.get('Name'))



#Users = r'C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Users.csv'
Users = r"C:\Users\Biowa\Desktop\Computer-Science-Programming-Projects\Program\Users.csv"
with open(Users) as People:
    UsersReader = csv.reader(People)
    UserArray = list(UsersReader)
# print(UserArray)


