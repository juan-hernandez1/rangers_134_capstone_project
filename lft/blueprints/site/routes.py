from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user



# internal imports
from lft.models import Exercise, db
from lft.helpers import get_exercises
from lft.forms import SetsRepsForm


# need to instantiate our Blueprint class
site = Blueprint('site', __name__, template_folder='site_templates' )



# use site object to create our routes
@site.route('/')
def lft():
    return render_template('lft.html') # looking inside our template_folder (site_templates) to find our lft.html file

# route to display "the vault" page
@site.route('/vault')
def vault():
    return render_template('vault.html')

# route to handle form submission in "the vault"
@site.route('/search', methods=['POST'])
def search():
    body_part = request.form.get('body_part') # it was ['body_part] before adding equipment
    equipment = request.form.get('equipment')
    exercises = get_exercises(body_part, equipment)
    form = SetsRepsForm()
    
    return render_template('vault.html', exercises = exercises, form = form, selected_body_part = body_part, selected_equipment = equipment)


# route to display "the lab" page with workouts
@site.route('/workout')
def lab():
    workouts = Exercise.query.filter_by(user_id=current_user.user_id)
    return render_template('workout.html', workouts = workouts)


# route to handle adding a workout
@site.route('/add_workout/<id>/<name>/<body_part>/<equipment>/<target>', methods=['GET', 'POST'])
def add_workout(id, name, body_part, equipment, target):
    if request.method == 'POST':
        # Handle the POST request
        exercise_id = id
        exercise_name = name
        body_part = body_part
        equipment = equipment
        gif_url = request.args.get("gif_url")
        target = target
        sets = request.form.get('sets')
        reps = request.form.get('reps')
        user_id = current_user.user_id

        print(gif_url)
        print(f"Exercise ID: {exercise_id}")
        print(f"Exercise Name: {exercise_name}")
        print(f"Sets: {sets}")
        print(f"Repetitions: {reps}")

        if not (exercise_id and sets and reps):
            flash("Error: Please fill in all required fields.", category='error')
            return redirect('/vault')
    
        # Create or update your Exercise object with the retrieved exercise
        # exercise = Exercise(id, body_part, equipment, name, target, sets, reps, user_id)
        
        

        # Checks if an exercise with the same name, body part, and equipment already exists for the user
        existing_exercise = Exercise.query.filter_by(
            name=exercise_name,
            # body_part=body_part,
            # equipment=equipment,
            user_id=user_id
        ).first()

        if existing_exercise:
            # Exercise already exists, you can choose to update it or skip the addition
            # For example, updating sets and reps
            existing_exercise.sets = sets
            existing_exercise.repetitions = reps

            db.session.commit()

            flash(f"You have successfully updated {exercise_name} in your workout", category='success')

        else:
            # Exercise doesn't exist, add it to the database
            exercise = Exercise(id, body_part, equipment, name, target, sets, reps, user_id, gif_url)
            db.session.add(exercise)
            db.session.commit()
            flash(f"You have successfully added {exercise_name} to your workout", category='success')

        return redirect('/workout')

    else:
        # Handle the GET request (if needed)
        # For example, render a form for selecting exercises
        exercises = Exercise.query.all()
        return render_template('vault.html', exercises = exercises)


# route to handle updating a workout
@site.route('/update_workout/<exercise_id>', methods=['GET', 'POST'])
def update_workout(exercise_id):

    # let's grab the specific workout that we want to update
    exercise = Exercise.query.get(exercise_id)

    if request.method == 'POST':
        exercise.sets = int(request.form['sets'])
        exercise.repetitions = int(request.form['repetitions'])

        db.session.commit()

        flash(f"You have successfully updated {exercise.name} in your workout", category='success')
        return redirect('/workout')

    return render_template('update_workout_form.html', exercise = exercise)
    

# route to handle deleting a workout
@site.route('/delete_workout/<exercise_id>')
def delete_workout(exercise_id):
    
    # query our database to find the object we want to delete
    exercise = Exercise.query.get(exercise_id)

    db.session.delete(exercise)
    db.session.commit()
    
    flash(f"You have successfully deleted {exercise.name} from your workout", category='success')
    return redirect('/workout')