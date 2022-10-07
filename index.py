import requests
import random


def triv():
  rand = random.randint(0, 3)
  r = requests.get('https://the-trivia-api.com/api/questions?limit=1')
  DATA = r.json()[0]
  QUESTION = DATA['question']
  WRONG = DATA['incorrectAnswers']
  CORRECT_ANSWER = DATA['correctAnswer']
  # ANSWER = 
  print(QUESTION , WRONG , CORRECT_ANSWER) 
triv()
