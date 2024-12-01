# Basic CRUD operations in MongoDB
from pymongo import MongoClient
con = MongoClient("localhost", 27017)
db = con.user_management
user_table = db.users
while True:
    print("Menu...")
    print("1) Create record")
    print("2) Read record")
    print("3) Update record")
    print("4) Delete record")
    print("5) Exit")
    user_inp = int(input("Enter your choice: "))
    [1, 2, 3, 4, 5].index(user_inp)  # will throw error if entered some other number
    if user_inp == 1:
        name = input("Enter your name: ")
        user_table.insert_one({"name": name})
    if user_inp == 2:
        users = user_table.find()
        for u in users:
            print(f"Name: {u["name"]}")
    if user_inp == 3:
        name = input("Enter the name of the user which you want to update: ")
        changed_name = input("Enter the name you want to change: ")
        user_table.update_one({"name": name}, {'$set': {'name': changed_name}})
    if user_inp == 4:
        name = input("Enter the name of the user which you want to delete: ")
        user_table.delete_one({'name': name})
    if user_inp == 5:
        break
