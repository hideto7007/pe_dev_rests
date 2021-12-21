from django.urls import path
from rest.test_restapi import views

urlpatterns = [
    path('rest/', views.ListView.as_view(), name='list'),
    path('rest/<int:px>', views.ListView.as_view(), name='detail'),
]
