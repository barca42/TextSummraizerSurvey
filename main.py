from flask import Flask, render_template, request
import pandas as pd
from database import db, Answer, AnswerType
from uuid import uuid4


questions = pd.read_csv('data/questions.csv')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        sample_questions = questions.sample(4)
        return render_template("survey.html", questions=sample_questions.to_dict('records'))
    if request.method == "POST":
        user_id = str(uuid4())
        for key,value in request.form.items():
            question_id=int(key.replace('-summary',''))
            answer = Answer(question_id=question_id,answer=AnswerType[value],user_id=user_id)
            db.session.add(answer)

        db.session.commit()
        return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)