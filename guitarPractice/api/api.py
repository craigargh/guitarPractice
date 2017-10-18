import jsonpickle
from flask import Flask
from flask_cors import CORS

from guitarPractice.exercises.exercises import make_exercise

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

    finally:
        return response


if __name__ == '__main__':
    app.run()
