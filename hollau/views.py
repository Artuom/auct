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
        form = forms.Lot(request.POST)
        # print request.user.id
        # print dir(request.session)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            description = data['description']
            start_price = data['start_price']
            start_date = data['start_date']
            end_date = data['end_date']
            category = data['category']
            models.Lot.objects.create(
                name=name,
                description=description,
                start_price=start_price,
                start_date=start_date,
                end_date=end_date,
                author=request.user,
                category=category,
            )
            return HttpResponse('Ok')
        else:
            return HttpResponse('NOK')
    else:
        context = {}
        return render(request, 'add_lot_form.html', {'form': forms.Lot})


def section_check(request):
    section = request.GET.get('section')
    print section
    section_qw = models.Category.objects.get(name__icontains=section[1:-2].lower())
    if section == section_qw.lower():
        value = section
    else:
        value = (1, 2, 3)
    data = {'value': value}
    print data
    return JsonResponse(data)


def add_category(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        return render(request, 'addcategory.html', {'form': forms.CategoryAdd(), 'categories': categories})
    else:
        form = forms.CategoryAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category_name = data['name']

            try:
                models.Category.objects.get(name=category_name)
            except ObjectDoesNotExist:
                models.Category.objects.create(name=category_name)
        return render(request, 'addcategory.html', {'form': forms.CategoryAdd(), 'categories': categories})


def lot_edit(request, pk):
    try:
        lot = models.Lot.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse('No such lot')
    if request.user == lot.author:
        if request.method == 'GET':
            return render(request, 'editLot.html', {'form': forms.Lot(instance=lot), 'pk': pk
                                                    })
        else:
            form = forms.Lot(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                lot.name = data['name']
                lot.description = data['description']
                lot.start_price = data['start_price']
                # lot.start_date = data['start_date']
                lot.end_date = data['end_date']
                lot.save()
                return HttpResponse('Your lot was edited')
    else:
        return HttpResponse("You can't edit this lot")


def lot_detail(request, pk):
    lot = models.Lot.objects.get(pk=pk)
    can_bet = (request.user != lot.author)
    categories = models.Category.objects.all()
    return render(request, 'lot_detail.html', {'lot': lot, 'pk': pk, 'can_bet': can_bet,
                                               'categories': categories})


def category(request, pk):
    categories = models.Category.objects.all()
    category_lots = models.Lot.objects.filter(category=pk)
    return render(request, 'categorypage.html', {'category_lots':category_lots,
                                                 'categories': categories})


def make_bet(request):
    pk = request.GET.get('pk')
    lot = models.Lot.objects.get(pk=pk)
    print lot.current_price
    if not lot.current_price:
        lot.current_price = 0.9 * lot.start_price
    else:
        lot.current_price = 0.9 * lot.current_price
    lot.save()
    data = {'current_price': lot.current_price}
    return JsonResponse(data)


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


def test_check(request):
    if request.method == 'GET':
        return render(request, 'autocheck.html', {})


def check_update(request):
    lot_id = 0
    data = request.GET.get('lot_id')
    print lot_id
    data = {
        'lot_id': lot_id
    }
    return JsonResponse(data)