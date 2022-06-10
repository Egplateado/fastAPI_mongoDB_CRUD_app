#import statements
from turtle import st
from bson import ObjectId
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity , listOfStudentEntity
from bson import objectid
student_router = APIRouter()

@student_router.get('/hello')
async def Hello():
    return "Hello Omar"
#getting all students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())
#get one student with matching ID
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id":ObjectId(studentId)}))

#createing a student
@student_router.post('/students')
async def create_student(student:Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

#update a student
@student_router.put('/students/{studentId}')
async def update_student(studentId , student:Student):
    #find the student and then update with new student data
    connection.local.student.find_one_and_update(
      {"_id":ObjectId(studentId)},
      {"$set":dict(student)}
    
    )
    return  studentEntity(connection.local.student.find_one({"_id":ObjectId(studentId)}))

#delete a student 
@student_router.delete('/student/{studentId}')
async def delete_student(studentId):
    #finds the students deletes it and also returns the same student objects
    return studentEntity(connection.local.student.find_one_and_delete({"_id":ObjectId(studentId)}))