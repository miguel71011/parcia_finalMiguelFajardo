from flask import  request
from flask.json import jsonify
from src import app
from src.models.sessions import SessionsModel
from src.models.slots import SlotsModel
slotModel = SlotsModel()
sessionsModel = SessionsModel()

@app.route('/slots/<idSlot>/sessions', methods=['POST','GET'])
def sessions(idSlot):
    

    if request.method == 'GET':
        #sessions = sessionsModel.getSessions(idSlot)
        sessions = sessionsModel.getSessions(idSlot)
        if len(sessions)== 0:
            return jsonify({'error':'No hay sesiones'})

        print(sessions)
        listSessions = []
        for session in sessions:
            listSessions.append({
                'id':session[0],
                'nombre':session[2],
                'fecha_hora_inicio':str(session[3]),
                'fecha_hora_final':str(session[4])
            })
        return jsonify({
            'materia':{
                'id':sessions[0][8],
                'nombre':sessions[0][9],
                'semestre':sessions[0][6]
            },
            'sesiones':listSessions
        })
    
    name = request.json['nombre']
    dateStart = request.json['fecha_hora_inicio']
    dateEnd = request.json['fecha_hora_final']
    sessionsModel.postSession(idSlot, name, dateStart, dateEnd)

    session=sessionsModel.getlastSession()
    students = slotModel.getStudentSlot(idSlot)
    slot = slotModel.getSlot(idSlot)
    for student in students:
        sessionsModel.postAssistances(session[0],student[3])
    #print(name, dateStart, dateEnd)
    return jsonify({
        'mensaje':'Sesion registrada',
        'sesion': {
            'id':session[0],
            'nombre':session[2],
            'fecha_hora_inicio':session[3],
            'fecha_hora_final':session[4]
        },
        'materia':{
            'id':slot[0],
            'nombre':slot[1],
            'semestre':slot[3]
        }
    })

@app.route('/sessions', methods=['GET'])
def getSessions():
    sessions = sessionsModel.allSessions()
    listSessions = []
    for session in sessions:
        listSessions.append({
            'id':session[0],
            'nombre':session[2],
            'fecha_hora_inicio':session[3],
            'fecha_hora_final':session[4]
        })
    return jsonify({
        'sessions':listSessions
    })


@app.route('/sessions/<idSession>/students', methods=['GET'])
def getStudentsSession(idSession):
    
    students = sessionsModel.getStudentsSession(idSession)
    if len(students) == 0:
        return jsonify({
            'error':'No hay estudiantes por mostrar'
        })

    listStudents = []
    for student in students:
        check = 'Confirmado'
        if student[7] == '0':
            check = 'http://127.0.0.1:5000/sessions/'+str(student[10])+'/students/'+str(student[0])
        print(student[7])
        #else:
            #check = 'Confirmado'
        listStudents.append({
            'id':student[0],
            'nombre':student[2],
            'identificacion':student[1],
            'apellido':student[3],
            'telefono':student[4],
            'email':student[5],
            'confirmar_asistencia':check
        })
        

    return jsonify({
        'sesion':{
            'id':students[0][10],
            'nombre':students[0][12],
            'fecha_hora_inicio':students[0][13],
            'fecha_hora_final':students[0][14]
        } ,
        'estudiantes':listStudents
    })

@app.route('/sessions/<idSession>/students/<idStudent>', methods=['PUT'])
def putAssistance(idSession, idStudent):
    sessionsModel.putAssistances(1,idSession,idStudent)

    return jsonify({
        'mensaje':'Confirmado'
    })
