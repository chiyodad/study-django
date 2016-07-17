# from django.shortcuts import render

from django.conf.urls import url
from django.contrib import admin

from django.views.generic import ListView, DetailView #generic view 사용
from bookmark.models import Bookmark

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark
