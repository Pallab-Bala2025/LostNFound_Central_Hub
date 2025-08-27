from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_item, name='dashboard'),
    path('hub/', views.central_hub, name='central_hub'),
]
