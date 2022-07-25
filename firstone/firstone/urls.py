
from django.contrib import admin
from django.urls import path
from . import new   

urlpatterns = [
    path('', new.news), path('twone/',new.twone), 
]
