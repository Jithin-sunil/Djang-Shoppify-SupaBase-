from django.urls import path
from Shop import views
app_name='Shop'
urlpatterns=[
    path('homepage/',views.homepage,name='homepage'),
    path('profile/',views.profile,name='profile'),
]