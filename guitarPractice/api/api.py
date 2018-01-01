import jsonpickle
from flask import Flask
from flask_cors import CORS

from guitarPractice.exercises.exercise_factory import make_exercise, list_exercises

app = Flask(__name__)
CORS(app)


@app.route('/exercise/<exercise_name>/<int:difficulty>', strict_slashes=False)
def get_exercise(exercise_name, difficulty):
    try:
        exercise = make_exercise(exercise_name, difficulty)

    except ValueError as value_error:
        response = app.response_class(
            response=str(value_error),
            status=404
        )

    else:
        exercise_json = jsonpickle.encode(exercise, unpicklable=False)

        response = app.response_class(
            response=exercise_json,
            status=200,
            mimetype='application/json'
        )

    return response


@app.route('/exercises/', strict_slashes=False)
def exercises():
    exercise_list = list_exercises()

    exercises_dicts = [
        exercise.to_dict()
        for exercise in exercise_list
    ]

    exercises_json = jsonpickle.encode(exercises_dicts, unpicklable=False)

    response = app.response_class(
        response=exercises_json,
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run()
