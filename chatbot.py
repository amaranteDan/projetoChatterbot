from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

chatbot = ChatBot('BotPtb')

conversa = [
    "Coe",
    "E ai, tranquilo?",
    "Tranquilo",
    "Qual a boa de hoje?",
    "São Paulo eliminado de novo",
    "Então nenhuma novidade kkk",
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)

chatbot.get_response("Coe")