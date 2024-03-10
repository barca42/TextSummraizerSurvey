from flask import Flask, render_template, request
import pandas as pd

questions = pd.read_csv('data/questions.csv')

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        sample_questions = questions.sample(4)
        return render_template("survey.html", questions=sample_questions.to_dict('records'))
    if request.method == "POST":
        print(request.form)
        return render_template("thankyou.html")