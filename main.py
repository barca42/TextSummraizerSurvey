from flask import Flask, render_template, request
import pandas as pd
from database import db
import os.path

questions = pd.read_csv('data/questions.csv')

app = Flask(__name__)

path = os.path.join('.','out','data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///out/data.db'

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        sample_questions = questions.sample(4)
        return render_template("survey.html", questions=sample_questions.to_dict('records'))
    if request.method == "POST":
        print(request.form)
        return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)