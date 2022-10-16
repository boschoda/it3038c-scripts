from peewee import *

db = SqliteDatabase('UCSchedule.db')

class BaseModel(Model):
    class Meta:
        database = db

class Student(BaseModel):
    student = CharField(unique=True)

class Classes(BaseModel):
    studentname = ForeignKeyField(Student)
    classname = CharField(unique=True)

db.connect()
db.create_tables([Student,Classes])

dora = Student.create(student = 'boschoda')
lara = Student.create(student = 'boschola')

dora.save()
lara.save()

Classes.create(studentname = dora, classname = 'SCRIPTING')
Classes.create(studentname = lara, classname = 'BIOLOGY')

Student.get(Student.student == dora)
Student.get(Student.student == lara)
