from django.urls import path

from . import views

app_name = 'studentcourseapp'
urlpatterns = [
    path('', views.index, name='index')
]
