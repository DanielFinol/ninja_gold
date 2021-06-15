from django.shortcuts import render, HttpResponse, redirect
from random import randint

def index(request):
    context = {'oro': request.session.get('oro', 0)}
    context['historial'] = request.session.get('historial', '')
    return render(request, 'ninja_gold.html', context)

def procesar(request):
    límites = request.POST['valor'].split()
    gana = randint(int(límites[0]), int(límites[1]))
    request.session['oro'] = request.session.get('oro', 0) + gana

    kdna = f'\n{gana:3} {"ganados" if gana >= 0 else "predidos"} en {límites[2]}\n'
    request.session['historial'] = request.session.get('historial', '') + kdna
    
    return redirect('/')

def reset(request):
    request.session['oro'] = 0
    request.session['historial'] = ''
    return redirect('/')
