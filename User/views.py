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

from django.shortcuts import render
from supabase import create_client


def change_password(request):
    user=tbl_user.objects.get(user_id=request.session.get('uid'))
    email=user.user_email
    if email:

        # Send a password reset email using Supabase
        try:
            response = supabase.auth.api.reset_password_for_email(email)
            if response.get("error"):
                return render(request, 'User/MyProfile.html', {'error': response["error"]["message"]})
            
            return render(request, 'User/MyProfile.html', {'message': 'Password reset email sent successfully. Check your inbox.'})
        except Exception as e:
            return render(request, 'User/MyProfile.html', {'error': str(e)})
    