from peewee import *

db = SqliteDatabase('UCSchedule.db')

class BaseModel(Model):
    class Meta:
        database = db

class Student(BaseModel):
    student = CharField(unique=True)

class Classes(BaseModel):
    studentname = ForeignKeyField(Student, backref='classes')
    classname = CharField(unique=True)

db.connect()
db.create_tables([Student,Classes])

dora = Student.create(studentname = 'boschoda')
lara = Student.create(studentname = 'boschola')

dora = Classes.create(classname = 'SCRIPTING')
lara = Classes.create(classname = 'BIOLOGY')
lara = Classes.create(classname = 'CHEMISTRY')

dora.save()
lara.save()

Student.get(Student.student == 'dora')
