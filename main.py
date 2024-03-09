from flask import Flask, render_template
import pandas as pd

questions = pd.read_csv('data/questions.csv')

app = Flask(__name__)


@app.route('/')
def hello_world():
    sample_questions = questions.sample(3)

    return render_template('survey.html', questions=sample_questions.to_dict('records'))
