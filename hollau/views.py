# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from hollau import models
import json as simplejson
from hollau import forms
from django.http import Http404


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
            # start_date = data['start_date']
            end_date = data['end_date']
            category = data['category']
            models.Lot.objects.create(
                name=name,
                description=description,
                start_price=start_price,
                # start_date=start_date,
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
    print request.user
    lot = models.Lot.objects.get(pk=pk)
    can_bet = (request.user != lot.author)
    categories = models.Category.objects.all()
    return render(request, 'lot_detail.html', {'lot': lot, 'pk': pk, 'can_bet': can_bet,
                                               'categories': categories})


def category(request, pk):
    categories = models.Category.objects.all()
    category_lots = models.Lot.objects.filter(category=pk).order_by('-start_date')
    paginator, page = paginate(request, category_lots)
    return render(request, 'categorypage.html', {'paginator': paginator, 'page': page, 'category_lots': page.object_list, 'categories': categories, 'category_id': pk})


def my_bets(request):
    user = request.user
    my_bet_lots = models.Bet.objects.filter(person=user)
    categories = models.Category.objects.all()
    my_lots = [my_bet.lot for my_bet in my_bet_lots]
    paginator, page = paginate(request, my_lots)
    return render(request, 'my_lot.html', {'paginator': paginator, 'page': page, 'my_lots': page.object_list, 'categories': categories})


def my_lots(request):
    my_lots = models.Lot.objects.filter(author=request.user)
    categories = models.Category.objects.all()
    paginator, page = paginate(request, my_lots)
    return render(request, 'my_lot.html', {'paginator': paginator, 'page': page, 'my_lots': page.object_list, 'categories': categories})


def make_bet(request):
    pk = request.GET.get('pk')
    lot = models.Lot.objects.get(pk=pk)
    print request.user
    if request.user != lot.author and request.user.is_authenticated:
        print 'ok'
        if not lot.current_price:
            lot.current_price = 0.9 * lot.start_price
        else:
            lot.current_price = 0.9 * lot.current_price
        bet = models.Bet.objects.create(lot=lot, price=lot.current_price, person=request.user)
        lot.save()
        data = {'current_price': lot.current_price}
    else:
        data = {'current_price': None}
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
    pk = request.GET.get('pk')
    lot = models.Lot.objects.filter(pk=pk).get()
    print lot
    bet = models.Bet.objects.filter(lot=lot).order_by('-date').first()
    data = {'end_date': lot.end_date, 'current_price': lot.current_price, 'bet': bet.date}
    return JsonResponse(data)


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 2))
    except ValueError:
        limit = 2
    if limit > 2:
        limit = 2
    try:
        page = int(request.GET.get('page',1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page


def testpagination(request):
    lots = models.Lot.objects.all().order_by('-start_date')
    paginator, page = paginate(request, lots)
    return render(request, 'testpagepagination.html', {'paginator': paginator, 'page': page, 'lots': page.object_list, 'count': [1,2]},)
    