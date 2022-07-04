from pymongo import MongoClient
 
try:
    conn = MongoClient()
    print("\nConnected successfully!!!")
except: 
    print("\nCould not connect to MongoDB")

url = "mongodb+srv://admin:admin@cluster0.31kvgex.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)
db = client.pytech

students = db.students

oakenshield = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield"
    }

oakenshield_student_id = students.insert_one(oakenshield).inserted_id

baggins = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins"
    }

baggins_student_id = students.insert_one(baggins).inserted_id

froggins = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Froggins"
    }

froggins_student_id = students.insert_one(froggins).inserted_id

print(f"\n-- INSERT STATEMENTS --")
print(f"\nInserted student record Thorin Okenshield into the students collection with document_id", oakenshield_student_id)
print(f"\nInserted student record Bilbo Baggins into the students collection with document_id", baggins_student_id)
print(f"\nInserted student record Frodo Baggins into the students collection with document_id", froggins_student_id)