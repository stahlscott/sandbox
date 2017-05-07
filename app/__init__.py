from decimal import Decimal
from flask import Flask, render_template, request, flash

from app.pw_gen import PasswordGenerator
from app.workout_calc import WorkoutCalculator

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/workout', methods=['POST', 'GET'])
def workout_calc():
    workout_calculator = WorkoutCalculator()
    if request.method == 'POST':
        data = request.form
        multiplier = Decimal(data['multiplier']) if data['multiplier'] else 1
        workout_list = workout_calculator.get_workout(multiplier=multiplier)
    else:
        workout_list = workout_calculator.get_workout(multiplier=1)
    return render_template('workout.html', workout_list=workout_list)


@app.route('/pw_gen', methods=['GET'])
def password_generator():
    pw_gen = PasswordGenerator()
    passphrase = pw_gen.get_random_passphrase()
    return render_template('pw_gen.html', passphrase=passphrase)
