from django.urls import path

# urls
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video/<str:room>/<str:created>/', views.video, name='video'),
]
