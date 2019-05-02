from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.upload, name='upload'),
    path('', views.list_docs, name='list'),
]
