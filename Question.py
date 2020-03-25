import mysql.connector

class Question:
  def __init__(self, text, choices, correct):
    self.text = text
    self.choices = choices
    self.correct = correct

def setupQuestions(mycursor):
  questions = []
  mycursor.execute("SELECT * FROM audrey_trivia")

  myresult = mycursor.fetchall()

  for q in myresult:
    questions.append(
      Question(q[1], (q[2], q[3], q[4], q[5]), q[6])
    )
  return questions