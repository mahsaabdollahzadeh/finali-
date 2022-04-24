

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('centeral', flyviewset.as_view({
        'post' : list
    })),

]
