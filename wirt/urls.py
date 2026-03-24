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

    # Page for adding a new Topic
    path('new_topic/', views.new_topic, name = 'new_topic'),

    # Page for adding a new entry
    path ('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry' )
]