from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from hollau.models import UserProfile
import json as simplejson

def index(request):
    return HttpResponse('You are welcome to hollau site!')


def login(request):
    print request.user.id
    return render_to_response('login.html', {'user': request.user})


@login_required(login_url='/')
def home(request):
    return render_to_response('home.html', {'user': request.user})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login')


def add_lot(request):
    if request.method == 'POST':
        pass
    else:
        context = {}
        return render(request, 'add_lot_form.html', context)


def make_bet(request):
    if request.method == 'POST':
        pass


def test_ajax(request):
    context = {}
    try:
        data = request.POST['text'].strip()
    except:
        context['text'] = 'error'
    else:
        context['text'] = data[::-1]
    return render_to_response('testtemplate.html', {})
