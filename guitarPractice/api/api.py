import jsonpickle
from flask import Flask
from flask_cors import CORS

from guitarPractice.exercises.arpeggio_picking import level_one

app = Flask(__name__)
CORS(app)


@app.route('/exercise/<exercise_name>/<difficulty>', strict_slashes=False)
def get_exercise(exercise_name, difficulty):
    exercise = level_one()
    exercise_json = jsonpickle.encode(exercise, unpicklable=False)

    response = app.response_class(
        response=exercise_json,
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run()
