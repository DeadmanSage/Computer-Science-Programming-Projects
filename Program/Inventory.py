import csv

Inventory = r'C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Inventory .csv'
with open(Inventory) as Equipment:
    InventoryReader = csv.reader(Equipment)
    InventoryArray = list(InventoryReader)
print(InventoryArray)



Users = r'C:\Users\stu-dyer.b\OneDrive - Brighter Futures Learning Partnership Trust\Documents\GitHub\Computer-Science-Programming-Projects\Program\Users.csv'
with open(Users) as People:
    UsersReader = csv.reader(People)
    UserArray = list(UsersReader)
print(UserArray)
