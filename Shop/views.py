from django.shortcuts import render
from django.conf import settings
from Guest.models import *
from supabase import create_client
# Create your views here.

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def homepage(request):
    shop=tbl_shop.objects.get(shop_id=request.session.get('sid'))
    shopname=shop.shop_name
    return render(request,'Shop/Homepage.html',{'shop':shopname})

def profile(request):
    shop=tbl_shop.objects.get(shop_id=request.session.get('sid'))
    return render(request, 'Shop/MyProfile.html',{'shop':shop})