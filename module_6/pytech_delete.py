from pymongo import MongoClient
url = "mongodb+srv://Bekkah93:Severus1993.@cluster0.vygwbkg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient (url)
students = client.pytech.students
docs=students.find({})
print ('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')
for doc in docs:
    print (f'Student ID: {doc["student_id"]}')
    print (f'First Name: {doc["first_name"]}')
    print (f'Last Name: {doc["last_name"]}')
    print ()

becky = {
 'first_name': 'Becky',
 'last_name': 'Strange',
 'student_id': 1010
}
becky_document_id = students.insert_one(becky).inserted_id
print(f'Inserted student record {becky["first_name"]} {becky["last_name"]} into the students collections with document id {becky_document_id}')
print ()
print ('-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')
doc =students.find_one({"student_id": 1010})
print (f'Student ID: {doc["student_id"]}')
print (f'First Name: {doc["first_name"]}')
print (f'Last Name: {doc["last_name"]}')
print()
students.delete_one({"student_id": 1010})

docs=students.find({})
print ('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')
for doc in docs:
    print (f'Student ID: {doc["student_id"]}')
    print (f'First Name: {doc["first_name"]}')
    print (f'Last Name: {doc["last_name"]}')
    print ()