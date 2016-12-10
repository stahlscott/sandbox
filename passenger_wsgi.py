from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def hello():
    return render_template('template.html',
                           my_string="Wheeeee!",
                           my_list=[0, 1, 2, 3, 4, 5])


@application.route('/template')
def basic_jinja():
    pass

if __name__ == "__main__":
    application.run()
