from django.shortcuts import render
from django.conf import settings
from Guest.models import *
from supabase import create_client
# Create your views here.

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def homepage(request):
    user=tbl_user.objects.get(user_id=request.session.get('uid'))
    username=user.user_name
    return render(request, 'User/Homepage.html',{'user':username})

def profile(request):
    user=tbl_user.objects.get(user_id=request.session.get('uid'))
    return render(request, 'User/MyProfile.html',{'user':user})