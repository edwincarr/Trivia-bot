import requests
import random

def triv():
  rand = random.randint(0, 3)
  r = requests.get('https://the-trivia-api.com/api/questions?limit=1')

  DATA = r.json()[0]
  QUESTION = DATA['question']
  CORRECT_ANSWER = DATA['correctAnswer']
  answers = DATA['incorrectAnswers']
  answers.insert(rand, CORRECT_ANSWER)

  print(QUESTION)
  print(answers)
  user_res = int(input('Give Correct Index: '))

  if answers[user_res] == CORRECT_ANSWER:
    print('Your cooking with gas')
  else:
    print(f'{CORRECT_ANSWER}... Try Again')

triv()
