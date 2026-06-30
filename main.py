from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):

          id: int
          name: str
          grade: int

# قاعدة البيانات المؤقتة لتخزين الطلاب
students = [
    Student(id=1, name="Alice", age=20, grade=90),
    Student(id=2, name="Bob", age=22, grade=80),
    Student(id=3, name="Charlie", age=21, grade=95)

]

# لقراءة جميع الطلاب
@app.get("/students")
async def read_students():
    return students 

#لانشاء طالب جديد
@app.post("/students")
async def create_student(student: Student):
    students.append(student)
    return student  

#تحدث طالب موجود
@app.put("/students/{student_id}")
async def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}

#لحذف طالب موجود
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)
            return deleted_student
    return {"error": "Student not found"}         