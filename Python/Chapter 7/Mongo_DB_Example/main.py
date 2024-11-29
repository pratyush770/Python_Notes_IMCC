# MongoDb can accept any columns i.e. columns can be different (Shape fluid)
# Primary Key is mandatory in MongoDb. It creates automatically (_id)
# There is no concept of foreign key in MongoDb
# MongoDb does not create a database, table unless it has atleast 1 record in it

# ORM(Object Relational Mapping) is an example of abstraction (Can be asked in interview)
# MongoClient gives access to database server
from pymongo import MongoClient
from db_demo import Student
from bson import ObjectId  # for passing ObjectId
con = MongoClient("localhost", 27017)  # download later to get the host and port number
db = con.db_demo  # db_demo is the database name which we created
db_table = db.demo_table  # demo_table is the table name which we created

name = input("Enter your name: ")  # take user input
age = int(input("Enter your age: "))
isIntelligent = input("Are you intelligent? ")
isIntelligent = isIntelligent.lower()
if isIntelligent == 'y':
    isIntelligent = True
elif isIntelligent == 'n':
    isIntelligent = False
else:
    print("Enter either y or n")

db_demo_dict = {
    "name": name,
    "age": age,
    "isIntelligent": isIntelligent
}

db_table.insert_one(db_demo_dict)  # insert one record

db_table.insert_many([   # we pass a list of dictionaries
    {"name": "Pankaj", "age": 21, "isIntelligent":True},
    {"naam": "Santosh", "umar": 24, "dimaagdar":True}
])

db_table.insert_many([   # we pass a method from modal class (db_demo)
    Student.values("Prayushi", 23, False),
    Student.values("Suchismita",47, True)
])

db_table.delete_one({'_id':ObjectId('6738af64e13a08863280ca00')})  # specify the id when installed

db_table.delete_many({"age":21})

entries = db_table.find()  # cursor named 'entries' is created
for e in entries:
    print(e)

entry = db_table.find_one()
print(entry)

db_table.update_one({'age': 23}, {'$set':{'name': 'Chaitanya'}})  # use $set to update the entry
db_table.update_many({'age': 20}, {'$set':{'name': 'Pratyush Majumdar'}})  # use $set to update the entries