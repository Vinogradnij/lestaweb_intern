from django.urls import path

from . import views

app_name = 'tfidf_table'

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]
