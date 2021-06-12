from flask import json, request,jsonify
from src import app
from src.models.students import StudentsModel
studentsModel = StudentsModel()

@app.route('/students', methods=['GET','POST'])
def getPoststudents():
    if request.method == 'GET':
        students = studentsModel.getStudents()
        listStudents = []
        for student in students:
            listStudents.append({
                'id':student[0],
                'nombre':student[2],
                'identificacion':student[1],
                'apellido':student[3],
                'telefono':student[4],
                'email':student[5]
            })
        return jsonify({
            "Estudiantes": listStudents
        })
    
    identification = request.json['identificacion']
    name = request.json['nombre']
    lastName = request.json['apellido']
    phone = request.json['telefono']
    mail = request.json['email']

    studentsModel.postStudent(identification, name, lastName, phone, mail)

    return jsonify({
        'mensaje': 'Guardado',
        'student': {
                'nombre':name,
                'identificacion':identification,
                'apellido':lastName,
                'telefono':phone,
                'email':mail
        }
    })

@app.route('/students/<idStudent>', methods=['PUT','DELETE'])
def deletePutstudents(idStudent):
    student = studentsModel.getStudent(idStudent)
    if student is None:
        return({
            'error':'No existe estudiante'
        })
    if request.method == 'DELETE':
        try:
            studentsModel.deleteStudent(idStudent)
        except:
            return({
                'error':'No se pudo eliminar el estudiante'
            })

        return jsonify({
            'mensaje':'Estudiante eliminado'
        })

    identification = request.json['identificacion']
    if identification == '':
        identification = student[1]

    name = request.json['nombre']
    if name == '':
        name = student[2]

    lastName = request.json['apellido']
    if lastName == '':
        lastName = student[3]

    phone = request.json['telefono']
    if phone == '':
        phone = student[4]

    mail = request.json['email']
    if mail == '':
        mail = student[5]

    studentsModel.putStudent(identification, name, lastName, phone, mail, idStudent)
    student = studentsModel.getStudent(idStudent)
    return jsonify({
        'mensaje': 'Datos actualizados',
        'estudiante':{
            'id':student[0],
            'nombre':student[2],
            'identificacion':student[1],
            'apellido':student[3],
            'telefono':student[4],
            'email':student[5]
        }
    })
