# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='profile')
    photo = models.TextField()


class Category(models.Model):
    name = models.CharField(u'Категория', max_length=30)

    def __unicode__(self):
        return self.name


class Lot(models.Model):
    name = models.CharField(u"предложение", max_length=100)
    description = models.TextField(u"описание предложения")
    # photo = models.ImageField(u"фотография", blank=True, upload_to='%Y-%m-%d')
    start_price = models.FloatField(u"стартовая цена")
    current_price = models.FloatField(u"текущая цена", blank=True, null=True)
    sold = models.BooleanField(u"продано", default=False)
    author = models.ForeignKey(User, verbose_name=u"Аукционатор", related_name='lots', default="1")
    start_date = models.DateTimeField(u'начало продажи', auto_now_add=True)
    end_date = models.DateTimeField(u'окончание продажи')
    lastest_propose = models.DateTimeField(u'последнее предложение', blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=u'Категория', default=1)

    class Admin:
        list_display = ("name", "price", "propose", "lastest_propose", "bought")
        ordering = ("-lastest_propose", "end_date",)

    def __unicode__(self):
        return self.name

    # class Meta:
    #     verbose_name = u'Лот'
    #     verbose_name_plural = u'Лоты'

    def propose(self):
        lastest = self.propose_set.order_by('-date')
        if lastest:
            return lastest[0]
        else:
            return None

    def bought(self):
        return self.propose() and ((self.end_date < datetime.datetime.now()) or self.sold)

    def get_end_date(self):
        return datetime.datetime.strftime(self.end_date, "%d.%m.%y, %H:%M")


class Bet(models.Model):
    lot = models.ForeignKey(Lot, verbose_name=u'лот')
    date = models.DateTimeField(u'дата', auto_now=True, editable=False)
    price = models.IntegerField(u"новая цена")
    person = models.ForeignKey(User)

    class Admin:
        list_display = ("lot", "price")

    class Meta:
        verbose_name = u"Ставка"
        verbose_name_plural = u"Ставки"

    def __unicode__(self):
        return self.person.username

    def get_date(self):
        return datetime.datetime.strftime(self.date, "%d.%m.%y, %H:%M")