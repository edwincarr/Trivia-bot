import requests

def triv():
  r = requests.get('https://the-trivia-api.com/api/questions?limit=1')
  DATA = r.json()[0]
  QUESTION = DATA['question']
  CORRECT_ANSWER = DATA['correctAnswer']
  # ANSWER = 

triv()
