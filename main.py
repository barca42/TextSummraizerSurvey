from flask import Flask, render_template, request
import pandas as pd
from database import db, Answer, AnswerType
from uuid import uuid4
import numpy
from sqlalchemy.sql import func


questions = pd.read_csv('data/questions.csv',index_col=0)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        result = db.session.query(Answer.question_id, db.func.count()).group_by(Answer.question_id)
        answer_counts = dict(result)
        answer_counts = {key: answer_counts.get(key, 0) for key in range(1, 16)}
        question_sample = sample_questions(answer_counts)

        return render_template("survey.html", questions=questions.loc[question_sample].to_dict('index'))

    if request.method == "POST":
        user_id = str(uuid4())
        for key,value in request.form.items():
            question_id=int(key.replace('-summary',''))
            answer = Answer(question_id=question_id,answer=AnswerType[value],user_id=user_id)
            db.session.add(answer)

        db.session.commit()
        return render_template("thankyou.html")


def sample_questions(answer_counts):
    maximum = max(answer_counts.values())

    weights_dict = {key:  3 ** (maximum - answer_counts[key]) for key in answer_counts.keys()}
    total = sum(weights_dict.values())
    keys = list(weights_dict.keys())
    probabilities = [weights_dict[key] / total for key in keys]
    question_numbers = (numpy.random.choice(a=keys, size=4, replace=False, p=probabilities))

    return question_numbers


if __name__ == "__main__":
    app.run(debug=True)