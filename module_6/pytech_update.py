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

students.update_one({'student_id': 1007}, {'$set': {'last_name': 'Smith'}})


print ('-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')
doc =students.find_one({"student_id": 1007})
print (f'Student ID: {doc["student_id"]}')
print (f'First Name: {doc["first_name"]}')
print (f'Last Name: {doc["last_name"]}')