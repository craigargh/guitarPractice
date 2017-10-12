import jsonpickle
from flask import Flask, jsonify

from guitarPractice.exercises.rhythm_arpeggios import level_one

app = Flask(__name__)


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
