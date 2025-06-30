# urls.py
from django.urls import path
from MyPlants import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]