from django.contrib import admin
from django.urls import path
from . import views

app_name ="testapp"

urlpatterns = [
    path('top/<int:param>', views.index, name='index'),
    path('top/', views.top, name='top'),
    path('settings/', views.settings, name='settings'),
]