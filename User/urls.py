from django.urls import path
from User import views
app_name='User'
urlpatterns=[
    path('homepage/',views.homepage,name='homepage'),
    path('profile/',views.profile,name='profile'),
    path('change_password/',views.change_password,name='change_password'),
]