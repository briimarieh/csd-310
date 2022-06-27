from pymongo import MongoClient
 
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")

url = "mongodb+srv://admin:admin@cluster0.31kvgex.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)
db = client.pytech

students = db.students

print(f"\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
docs = db.students.find({})
for doc in docs:
    print(f"\n Student ID: ", doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

deckard = {
    "student_id": "1010",
    "first_name": "Rick",
    "last_name": "Deckard"
    }

deckard_student_id = students.insert_one(deckard).inserted_id

print(f"\n-- INSERT STATEMENTS --")
print(f"\nInserted student record 1010 into the students collection with document_id", deckard_student_id)

print(f"\n-- DISPLAYING NEW STUDENT LIST DOC --")
docs = db.students.find({})
for doc in docs:
    print(f"\n Student ID: ", doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

result = db.students.delete_one({"student_id": "1010"})

print(f"\n-- DELETED STUDENT ID: 1010 --")
docs = db.students.find({})
for doc in docs:
    print(f"\n Student ID: ", doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")