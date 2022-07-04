from pymongo import MongoClient
 
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")

url = "mongodb+srv://admin:admin@cluster0.31kvgex.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)
db = client.pytech

print(f"\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
    print(f"\n Student ID: ", doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Batley"}})

print(f"\n-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": "1007"})
print(f"\n Student ID: ", doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")