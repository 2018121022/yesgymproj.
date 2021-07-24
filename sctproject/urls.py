"""sctproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import account.views as account
from blogapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = "home"),
    path('account/login',account.login_view, name="login"),
    path('account/logout', account.logout_view, name="logout"),
    path('account/register', account.register_view, name="register"),
    path('lesson/', lesson, name = "lesson"),
    path('comment/', comment, name = "comment"),
    path('write/', write, name = "write"),
    path('detail/<str:gym_id>', detail, name = "detail"),
    path('update/<str:gym_id>', update, name = "update"),
    path('delete/<str:gym_id>', delete, name = "delete"),
    path('content/', content, name = "content"),
]
