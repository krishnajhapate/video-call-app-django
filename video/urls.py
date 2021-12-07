from django.urls import path

# urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vide/<str:room>/<str:created>/', views.index, name='index'),
]
