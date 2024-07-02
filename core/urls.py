from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('signup/insertuser', views.insertuser, name='insertuser'), 
]