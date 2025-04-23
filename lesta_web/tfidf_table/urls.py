from django.urls import path

from . import views

app_name = 'tfidf_table'

urlpatterns = [
    path('', views.UploadFilesView.as_view(), name='index'),
]
