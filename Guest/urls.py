from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns=[
    
     path('user/',views.user,name="user"),
     path('shop/',views.shop,name="shop"),
  path('login/',views.login,name="login"),
  path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
]