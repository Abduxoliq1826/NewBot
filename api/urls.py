from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('add_student', AddStudent),
    path('science/', ViewsScience),
    path('info/', BotInfo),
    path('detail/', BotDetaill),
]