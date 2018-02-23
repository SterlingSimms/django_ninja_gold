from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
import random
from time import strftime
from models import *

def index(request):
    return render(request, 'gold/index.html')

def process(request):
    log = []
    randon_num = 0
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if request.POST['name'] == 'farm':
        random_num = random.randint(10, 21)
        request.session['gold'] = request.session['gold'] + random_num
        log.append('Earned {} gold from the farm! ({})'.format(random_num, strftime("%c")))
    if request.POST['name'] == 'cave':
        random_num = random.randint(5, 11)
        request.session['gold'] = request.session['gold'] + random_num
        log.append('Earned {} gold from the cave! ({})'.format(random_num, strftime("%c")))
    if request.POST['name'] == 'house':
        random_num = random.randint(2, 6)
        request.session['gold'] = request.session['gold'] + random_num
        log.append('Earned {} gold from the farm! ({})'.format(random_num, strftime("%c")))
    if request.POST['name'] == 'casino':
        random_num = random.randint(-50, 51)
        request.session['name'] = request.session['gold'] + random_num
        if(random_num >= 1):
            log.append('Earned {} gold from the casino! ({})'.format(random_num, strftime("%c")))
        else:
            log.append('Lost {} gold from the casino! Sorry! ({})'.format(random_num, strftime("%c")))
    if 'log' not in request.session:
        request.session['log'] = []
    else:
        request.session['log'] += log
    return redirect('/')
