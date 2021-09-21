from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    msg = ''
    if idade < 18:
        msg = 'menor de idade'
    else:
        msg = 'maior de idade'
    return HttpResponse(f'<h1>Hello {nome}! Você é {msg}</h1>')
