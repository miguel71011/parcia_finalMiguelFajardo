
from src.controllers import students
from flask import request,jsonify
from src import app
from src.models.slots import SlotsModel
from src.models.students import StudentsModel
from src.models.sessions import SessionsModel

sessionsModel = SessionsModel()
studentsModel = StudentsModel()
slotsModel = SlotsModel()

@app.route('/slots', methods=['GET','POST'])
def slots():
    if request.method == 'GET':
        slots = slotsModel.getSlots()
        listSlots = []

        for slot in slots:
            listSlots.append({
                'id': slot[0],
                'nombre': slot[1],
                'semestre': slot[3],
            })

        return jsonify({'materias':listSlots})

    name = request.json['nombre']
    semester = request.json['semestre']

    slotsModel.postSlot(name)
    slot = slotsModel.getLastSlot()
    slotsModel.postSemester(semester,slot[0])

    return jsonify({'materia':{
        'id': slot[0],
        'nombre': slot[1],
    }, 'message':'Guardado...'})


@app.route('/slots/<idSlot>/students/<idStudent>', methods=['POST', 'DELETE'])
def slotStudent(idSlot, idStudent):
    if request.method == 'DELETE':
        slotsModel.deleteStudentSlot(idStudent,idSlot)
        sessions = sessionsModel.getSessions(idSlot)
        for session in sessions:
            sessionsModel.deleteAssistances(session[0],idStudent)

        return jsonify({
            'mensaje':'Estudiante desmatriculado'
        })
    
    try:
        slotsModel.postStudentSlot(idStudent, idSlot)
    except:
        jsonify({
            'error':'No se pudo regitrar'
        })
    student = studentsModel.getStudent(idStudent)
    slot = slotsModel.getSlot(idSlot)
    sessions = sessionsModel.getSessions(idSlot)
    for session in sessions:
        sessionsModel.postAssistances(session[0],idStudent)
        
    print(sessions)
    return jsonify({
        'mensaje':'Guardado',
        'materia':{
            'id': slot[0],
            'nombre': slot[1],
            'semestre': slot[3],
        },
        'estudiante':{
            'id':student[0],
            'nombre':student[2],
            'identificacion':student[1],
            'apellido':student[3],
            'telefono':student[4],
            'email':student[5]
        }
    })

@app.route('/slots/<idSlot>/students', methods=['GET'])
def getSlotStudent(idSlot):

    studentsSlot = slotsModel.getStudentSlot(idSlot)
    listStudentsSlot = []
    for student in studentsSlot:
        listStudentsSlot.append({
            'id':student[3],
            'nombre':student[5],
            'identificacion':student[4],
            'apellido':student[6],
            'telefono':student[7],
            'email':student[8]
        })
    slot = slotsModel.getSlot(idSlot)
    return jsonify({
        'estudiantes':listStudentsSlot,
        'materia':{
            'id': slot[0],
            'nombre': slot[1],
            'semestre': slot[3],
        } 
    })
