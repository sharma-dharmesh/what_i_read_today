from django.urls import path

from . import views

app_name = 'wirt'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

]