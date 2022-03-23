from django.contrib import admin
from django.urls import path
from django.urls import include
from api.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]
