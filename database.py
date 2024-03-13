import enum

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AnswerType(enum.Enum):
    extractive = 'extractive'
    abstractive = 'abstractive'
    hybrid = 'hybrid'

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer)
    answer = db.Column(db.Enum(AnswerType))
    user_id = db.Column(db.String)


