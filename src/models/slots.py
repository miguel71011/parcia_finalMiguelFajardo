from src.config.db import DB

class SlotsModel():

    def getSlots(self):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM slots INNER JOIN semesters ON slots.slot_id = semesters.Slot_id')
        slots = cursor.fetchall()
        cursor.close()
        return slots

    def getSlot(self, idSlot):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM slots INNER JOIN semesters ON slots.slot_id = semesters.Slot_id where slots.Slot_id = ?',(idSlot,))
        slot = cursor.fetchone()
        cursor.close()
        return slot


    def getSlots(self):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM slots INNER JOIN semesters ON slots.slot_id = semesters.Slot_id')
        slots = cursor.fetchall()
        cursor.close()
        return slots



    def postSlot(self, name):
        cursor = DB.cursor()
        cursor.execute('insert into slots(name) values(?)',(name,))
        cursor.close()
    
    def getLastSlot(self):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM slots WHERE slot_id = (SELECT MAX(slot_id) FROM slots)')
        
        slot = cursor.fetchone()
        cursor.close()
        return slot
    
    def postSemester(self,semester, id_slots):
        cursor = DB.cursor()
        cursor.execute('insert into semesters(semester,slot_id) values(?,?)',(semester, id_slots,))
        cursor.close()

    def postStudentSlot(self, idStudent, idSlot):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO students_semesters(student_id, semester_id) VALUES(?,(SELECT Semester_id FROM semesters WHERE semesters.Slot_id = ?))',(idStudent,idSlot,))
        cursor.close()

    def deleteStudentSlot(self, idStudent, idSlot):
        cursor= DB.cursor()
        cursor.execute('DELETE from students_semesters WHERE student_id = ? and semester_id = (SELECT Semester_id FROM semesters WHERE Slot_id = ?)',(idStudent, idSlot,))
        cursor.close()

    
    def getStudentSlot(self, idSlot):
        cursor = DB.cursor()
        cursor.execute('SELECT slots.Slot_id, slots.name, s.semester, students.Student_id, students.identification, students.name, students.lastName, students.phone, students.mail FROM slots INNER JOIN semesters AS s ON slots.Slot_id = s.Slot_id INNER JOIN students_semesters as s_s ON s.Semester_id = s_s.semester_id INNER JOIN students ON s_s.student_id = students.Student_id WHERE slots.Slot_id = ?',(idSlot,))
        
        studentsSlot = cursor.fetchall()
        cursor.close()
        return studentsSlot