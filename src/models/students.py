from src.config.db import DB

class StudentsModel():

    def getStudents(self):
        cursor = DB.cursor()
        cursor.execute('select * from students')
        students = cursor.fetchall()
        cursor.close()
        return students

    def getStudent(self, idStudent):
        cursor = DB.cursor()
        cursor.execute('select * from students where Student_id = ?',(idStudent,))
        student = cursor.fetchone()
        return student



    def postStudent(self, identification, name, lastName, phone, mail):
        cursor = DB.cursor()
        cursor.execute('insert into students(identification, name, lastName, phone, mail) values(?,?,?,?,?)',(identification, name, lastName, phone, mail,))
        cursor.close()

    def putStudent(self, identification, name, lastName, phone, mail, idStudent):
        cursor = DB.cursor()
        cursor.execute('update students set identification=?, name=?, lastName=?, phone=?, mail=? where Student_id=?',(identification, name, lastName, phone, mail, idStudent,))
        cursor.close()

    def deleteStudent(self,idStudent):
        cursor = DB.cursor()
        cursor.execute('delete from students where Student_id = ?',(idStudent,))
        cursor.close()


   