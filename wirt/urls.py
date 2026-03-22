from django.urls import path

from . import views

app_name = 'wirt'

urlpatterns = [
    # Home Page
    path('', views.index, name = 'index'),

    # Topic Page
    path('topics/', views.topics, name = 'topics'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),

]