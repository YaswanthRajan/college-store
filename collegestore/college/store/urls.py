from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('register', views.demo, name='register'),
    path('login', views.login, name='login'),
    path('bio', views.detail, name='bio'),
    path('logout',views.logout, name='logout')
]
