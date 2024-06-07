from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    
    path('user/', views.user, name='user'),
    
    path('user/crear/', views.crear_user, name='crear_user'),
]
