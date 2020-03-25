import flask
from flask import request, session
from Game import *
from Question import *
import mysql.connector

app = flask.Flask(__name__)
app.secret_key = 'abcdefg'

db = mysql.connector.connect(
  host="104.168.136.69",
  user="yscbtlcv_teacher",
  passwd="TopCoder15",
  database="yscbtlcv_instructor"
)

mycursor = db.cursor()

questions = setupQuestions(mycursor)

users = 0


# tomas = yscbtlcv_cwktomas223
# nam = yscbtlcv_cwknam5783
# chi = yscbtlcv_cwkchi5781

@app.route('/', methods = ['GET', 'POST'])
def home():
  global users

  # if request.method == 'POST':
  #   print(session['gameIndex'])
  #   current = games[session['gameIndex']].current
  #   games[session['gameIndex']].current += 1
  #   choice = request.get_data()

  #   if int(choice) == questions[current].correct:
  #     games[session['gameIndex']].correct += 1

  #   if game[session['gameIndex']].current >= len(questions):
  #     return flask.render_template(
  #       'end.html', 
  #        correct = games[session['gameIndex']].correct,
  #        total = len(questions))
  # else:
  #   if not 'gameIndex' in session:
  #     session['gameIndex'] = users
  #     users += 1
  #   if not session['gameIndex'] in games:
  #     games.append(games())
  #     print(games)

  #   games[session['gameIndex']].current = 0
  #   games[session['gameIndex']].correct = 0


  return flask.render_template(
    'index.html',
    num = 1,
    question = questions[0])

if __name__ == "__main__":
  app.run(host="0.0.0.0")
