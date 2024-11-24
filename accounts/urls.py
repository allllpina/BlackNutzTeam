from django.urls import path
from .views import register
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        success_url='/profile/'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('success/', views.registration_success, name='success'),
    path('profile/', views.profile, name='profile'),
    path('recommendations/', views.recommend_movies, name='recommendations'),

]