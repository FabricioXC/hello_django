from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    msg = ''
    if idade < 18:
        msg = 'menor de idade'
    else:
        msg = 'maior de idade'
    return HttpResponse(f'<h1>Hello {nome}! Você é {msg}</h1>')

def operacoes(request, operacao, a, b):
    msg = ''
    total = 0
    if operacao not in ['soma', 'multiplicacao', 'divisao', 'subtracao']:
        return HttpResponse(f'<h1>A operação {operacao} não existe nesta aplicação.</h1>')

    if operacao == 'soma':
        total = a + b
    elif operacao == 'subtracao':
        total = a - b
    elif operacao == 'multiplicacao':
        total = a * b
    else:
        total = a / b
    
    return HttpResponse(f'<h1>A {operacao} entre {a} e {b} é {total}</h1>')

