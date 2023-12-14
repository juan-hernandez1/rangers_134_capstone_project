from flask import Blueprint, request, jsonify 
from flask_jwt_extended import create_access_token, jwt_required 
from lft.models import Exercise, db, exercise_schema, exercises_schema



api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/token', methods = ['GET', 'POST'])
def token():

    data = request.json
    if data:
        client_id = data['client_id']
        access_token = create_access_token(identity=client_id) # just needs a unique identifier 
        return {
            'status': 200,
            'access_token': access_token
        }
    else:
        return {
            'status' : 400,
            'message' : 'Missing Client Id. Try Again.'
        }
    

@api.route('/exercises')
@jwt_required()
def get_exercises():

    allexercises = Exercise.query.all()

    response = exercises_schema.dump(allexercises)
    return jsonify(response)


@api.route('/exercise', methods=['POST'])
@jwt_required()
def add_exercise():

    data = request.json

    new_exercise = Exercise(
        body_part=data['body_part'],
        equipment=data['equipment'],
        gif_url=data['gif_url'],
        name=data['name'],
        target=data['target'],
        sets=data['sets'],
        repetitions=data['repetitions'],
        user_id=data['user_id']
    )

    db.session.add(new_exercise)
    db.session.commit()

    return jsonify({'message': 'Exercise added successfully'})


@api.route('/exercise/<id>', methods=['PUT'])
@jwt_required()
def update_exercise(id):
    exercise = Exercise.query.get(id)

    if exercise:
        data = request.json
        exercise.body_part = data['body_part']
        exercise.equipment = data['equipment']
        exercise.gif_url = data['gif_url']
        exercise.name = data['name']
        exercise.target = data['target']
        exercise.sets = data['sets']
        exercise.repetitions = data['repetitions']
        
        db.session.commit()
        
        return jsonify({'message': 'Exercise updated successfully'})
    else:
        return jsonify({'message': 'Exercise not found'})
    

@api.route('/exercise/<id>', methods=['DELETE'])
@jwt_required()
def delete_exercise(id):
    exercise = Exercise.query.get(id)

    if exercise:
        db.session.delete(exercise)
        db.session.commit()

        return jsonify({'message': 'Exercise deleted successfully'})
    else:
        return jsonify({'message': 'Exercise not found'})
