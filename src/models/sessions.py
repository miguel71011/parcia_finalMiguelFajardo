from src.config.db import DB
class SessionsModel():
    def allSessions(self):
        cursor = DB.cursor()
        cursor.execute('select * from sessions')
        sessions = cursor.fetchall()
        return sessions


    def getSessions(self, idSlot):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM sessions INNER JOIN semesters ON sessions.semester_id = semesters.Semester_id INNER JOIN slots ON semesters.Slot_id = slots.Slot_id WHERE semesters.Slot_id = ?',(idSlot,))
        sessions = cursor.fetchall()
        cursor.close()
        return sessions

    def postAssistances(self, idSession, idStudent):
        cursor = DB.cursor()
        cursor.execute('insert into assistances(Session_id, Student_id) values(?,?)',(idSession,idStudent,))
        cursor.close()

    def postSession(self, idSlot, sessionName, date_start, date_end):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO sessions(semester_id, sessionName, date_start, date_end) VALUES((SELECT Semester_id FROM semesters WHERE semesters.Slot_id = ?),?,?,?)',(idSlot, sessionName, date_start, date_end,))
        cursor.close()

    def getlastSession(self):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM sessions WHERE Session_id = (SELECT MAX(Session_id) FROM sessions)')
        session = cursor.fetchone()
        cursor.close()
        return session

    def getStudentsSession(self, idSession):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM students INNER JOIN assistances ON students.Student_id = assistances.Student_id INNER JOIN sessions ON assistances.Session_id = sessions.Session_id WHERE assistances.Session_id = ?',(idSession,))
        students = cursor.fetchall()
        cursor.close()
        return students

    def deleteAssistances(self, idSession, idStudent):
        cursor = DB.cursor()
        cursor.execute('delete from assistances where Session_id = ? and Student_id= ?',(idSession,idStudent,))
        cursor.close()

    def putAssistances(self, check, idSession, idStudent):
        cursor = DB.cursor()
        cursor.execute('update assistances set assistanceCheck = ? where Session_id = ? and Student_id = ?',(check, idSession, idStudent,))
        cursor.close()
