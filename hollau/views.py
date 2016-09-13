# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from hollau import models
import json as simplejson
from hollau import forms

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
        return render(request, 'add_lot_form.html', {'form':forms.Lot})

def section_check(request):
    section = request.GET.get('section')
    print section
    section_qw= models.Category.objects.get(name__icontains=section[1:-2].lower())
    if section == section_qw.lower():
        value = section
    else:
        value = (1,2,3)
    data = {'value': value}
    print data
    return JsonResponse(data)


def add_category(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        return render(request, 'addcategory.html', {'form':forms.CategoryAdd(), 'categories':categories})
    else:
        form = forms.CategoryAdd(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print data
            category_name = data['name']
        
            try:
                models.Category.objects.get(name=category_name)
            except ObjectDoesNotExist:
                models.Category.objects.create(name=category_name)
        return render(request, 'addcategory.html', {'form':forms.CategoryAdd(), 'categories':categories})


def make_bet(request):
    if request.method == 'POST':
        pass


def test_form(request):
    if request.method == 'GET':
        return render(request, 'test.html', {})
    else:
        return HttpResponse('ok')


def test_ajax(request):
    username = request.GET.get('username', None)
    if username == 'Art'.lower():
        boolVal = True
    else:
        boolVal = False
    data = {
        'is_taken': boolVal
    }
    return JsonResponse(data)


def countdown(request):
    return render(request, 'countdown.html', {})
