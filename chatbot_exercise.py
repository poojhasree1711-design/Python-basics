from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("MyBot")

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

while True:
    user = input("You: ")
    response = bot.get_response("hi poojha")
    print("Bot:", response)