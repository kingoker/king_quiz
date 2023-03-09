from django.shortcuts import render
from .models import *
import requests
# Create your views here.
from king_quiz.settings import MEDIA_ROOT
import os
import pprint

admins = [1600170280, 2101666900, 99940983]

# Функция отправки смс в телеграм
def sendMessage(text, *args):
    method = 'https://api.telegram.org/bot5886372938:AAFiwOjZDjT4oIBa3X9RY1gf8DKYhFxpNIA/sendMessage'
    for chat_id in args[0]:
        requests.post(method, data={
            'chat_id': chat_id,
            'text': text
        })

def sendDocument(chat_id,file):
    path = MEDIA_ROOT/file
    print(path)
    bot_token = '5001491339:AAFeAZ9BG7x6PFFkYKXhCO7B8cxmgP3QaCg'
    send_document = 'https://api.telegram.org/bot' + bot_token +'/sendDocument?'
    data = {
        'chat_id': chat_id,
    }
    print(requests.post(send_document, data=data,files={"document": open(path, 'rb')}).json())

def index(request, token):
    try:
        quizzes = Quizzes.objects.filter(token=token).first();
        close_quiestion = quizzes.closequestions_set.all();
        open_quiestion = quizzes.openquestions_set.all();

        # list = []
        # for question,i in zip(close_quiestion, range(len(close_quiestion))):
        #     radio = question.radiotext_set.all()
        #     close_quiestion.values()[i] = 1
        #     print(close_quiestion.values()[i].extra('answer': radio.values()))


        # print(close_quiestion.values())
        # for quiestion in close_quiestion:
        #     radio = close_quiestion.radiotext_set.all();

        #     list.append(quiestion)

        one_list = list(close_quiestion.values()) + list(open_quiestion.values())
        
        quizzes_list = sorted(one_list, key=lambda x: x['order'])

        print(quizzes_list[0])
        

        context  = {
            'quizzes_list': quizzes_list,
        }

        return render(request, 'index.html',context)
    
    except:
        return render(request, 'index.html')


    