import requests

def triv():
  r = requests.get('https://the-trivia-api.com/api/questions?limit=1')
  data = r.json()
  print(data[0])


triv()
