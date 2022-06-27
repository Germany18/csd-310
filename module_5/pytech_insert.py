from pymongo import MongoClient
url = "mongodb+srv://Bekkah93:Severus1993.@cluster0.vygwbkg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient (url)
students = client.pytech.students
fred = {
 'first_name': 'Fred',
 'last_name': 'Weirdo',
 'student_id': 1007
}
bilbo ={
    'first_name': 'Bilbo',
    'last_name': 'Baggins',
    'student_id': 1008
}
iron ={
    'first_name': 'Iron',
    'last_name': 'Man',
    'student_id': 1009
}
 
fred_document_id = students.insert_one(fred).inserted_id
bilbo_document_id = students.insert_one(bilbo).inserted_id
iron_document_id = students.insert_one(iron).inserted_id
 
print ('-- INSERT STATEMENTS --')
print(f'Inserted student record {fred["first_name"]} {fred["last_name"]} into the students collections with document id {fred_document_id}')
print(f'Inserted student record {bilbo["first_name"]} {bilbo["last_name"]} into the students collections with document id {bilbo_document_id}')
print(f'Inserted student record {iron["first_name"]} {iron["last_name"]} into the students collections with document id {iron_document_id}')
