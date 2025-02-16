"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import update_balance

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('add_mission/', views.add_mission, name='add_mission'),
    path('delete_mission/<int:mission_id>/', views.delete_mission, name='delete_mission'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('delete_mission/', views.delete_mission, name='delete_mission'),
    path('edit_expense/', views.edit_expense, name='edit_expense'),
    path('delete_expense/', views.delete_expense, name='delete_expense'),
    path('edit_mission/', views.edit_mission, name='edit_mission'),
    path('delete_mission/', views.delete_mission, name='delete_mission'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
     path('update-balance/', update_balance, name='update_balance'),

]