# -*- coding: utf-8 -*-

from hollau.models import UserProfile, Lot, Bet, User, Category
from django import forms


class Lot(forms.ModelForm):
    class Meta:
        model = Lot
        fields = ['name', 'description', 'start_price', 'end_date', 'category', 'location']

class CategoryAdd(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class Bet(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['price']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions',
                   'password')

class TestForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)

class AdressForm(forms.Form):
    adress = forms.CharField(label='adress', max_length=100)