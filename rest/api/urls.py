from django.urls import path
from rest.api import views

urlpatterns = [
    path('rest/', views.ListView.as_view(), name='list'),
    path('rest/<int:px>', views.DetailView.as_view(), name='detail'),
]
