
from django.urls import path
from MyPlants import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('add-plant/', views.add_plant_view, name='add_plant'),
    path('profile/', views.profile_view, name='profile'),
    path('otp/', views.login_view, name='otp'),
]