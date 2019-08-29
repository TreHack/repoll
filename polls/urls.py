#!/usr/bin/python

#-*- coding:UTF-8 -*-

from django.urls import path
from . import views
from django.conf.urls import url, include


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<str:apptrye>/', views.run_scan_tomcat, name='run_scan_tomcat'),
    path('<int:year>/<int:month>/<slug:slug>/', views.url_test, name='url_test'),
    path(r'pyecharts/', views.pyecharts, name='pyecharts')
]