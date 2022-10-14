# import requests
# import random

# def triv():
#   rand = random.randint(0, 3)
#   r = requests.get('https://the-trivia-api.com/api/questions?limit=1')

#   DATA = r.json()[0]
#   QUESTION = DATA['question']
#   CORRECT_ANSWER = DATA['correctAnswer']
#   answers = DATA['incorrectAnswers']
#   answers.insert(rand, CORRECT_ANSWER)

#   print(QUESTION)
#   print(answers)
#   user_res = int(input('Give Correct Index: '))

#   if answers[user_res] == CORRECT_ANSWER:
#     print('Your cooking with gas')
#     return 1
#   else:
#     print(f'{CORRECT_ANSWER}... Try Again')
#     return 0

# def multiTriv(rounds = 3):
#   counter = 0
#   for x in range(rounds):
#     result = triv()
#     if result == 1:
#       counter += 1
#   print(f"Correct: {counter} out of {rounds}")

# multiTriv()


import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Connected!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)