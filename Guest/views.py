from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
import uuid
from django.conf import settings
from supabase import create_client
# Create your views here.

supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def ajaxplace(request):
    district_id = request.GET.get('did')
    place = tbl_place.objects.filter(district=district_id)
    print(place)
    return render(request, "Guest/AjaxPlace.html", {'place': place})

def user(request):
    dis = tbl_district.objects.all()
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            auth_response = supabase.auth.sign_up({
                "email": email,
                "password": password,
            })
            
            if auth_response.user:
                user_data = auth_response.user  
                user_id = user_data.id
                photo = request.FILES.get('photo')

                if photo:
                    try:
                        # File name uses only user_id and the original photo name
                        file_name = f"UserDocs/{user_id}_{photo.name}"
                        photo_content = photo.read()
                        storage_response = supabase.storage.from_("Shoppify").upload(file_name, photo_content)
                        photo_url = supabase.storage.from_("Shoppify").get_public_url(file_name)
                    except Exception as e:
                        return render(request, "Guest/User.html", {"district": dis, "error": "Failed to upload photo."})
                else:
                    photo_url = None  # Handle cases where no photo is uploaded
                
                # Save user details in the database
                tbl_user.objects.create(
                    user_id=user_id,
                    user_name=request.POST.get('name'),
                    user_email=email,
                    user_password=password,
                    user_address=request.POST.get('address'),
                    user_contact=request.POST.get('contact'),
                    user_photo=photo_url,
                    place=tbl_place.objects.get(id=request.POST.get('sel_place'))
                )
                
                return redirect('Guest:login')
            else:
                return render(request, "Guest/User.html", {"district": dis, "error": "Sign-up failed."})

        except Exception as e:
            return render(request, "Guest/User.html", {"district": dis, "error": "An error occurred during sign-up."})
    
    return render(request, "Guest/User.html", {"district": dis})




def shop(request):
    dis = tbl_district.objects.all()
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
           
            auth_response = supabase.auth.sign_up({
                "email": email,
                "password": password,
            })
            
            if auth_response.user:
                shop_data = auth_response.user  
                shop_id = shop_data.id
                place_id = request.POST.get('sel_place')
                photo = request.FILES.get('photo')

               
                try:
                    file_name = f"ShopDocs/{shop_id}_{uuid.uuid4()}_{photo.name}"
                    photo_content = photo.read()
                    storage_response = supabase.storage.from_("Shoppify").upload(file_name, photo_content)
                    photo_url = supabase.storage.from_("Shoppify").get_public_url(file_name)
                except Exception as e:
                    return render(request, "Guest/Shop.html", { "error": "Failed to upload photo."})

              
                tbl_shop.objects.create(
                    shop_id=shop_id,
                    shop_name=request.POST.get('name'),
                    shop_email=email,
                    shop_password=password,
                    shop_address=request.POST.get('address'),
                    shop_contact=request.POST.get('contact'),
                    shop_photo=photo_url,
                    place=tbl_place.objects.get(id=place_id)
                )
                
               
                return redirect('Guest:login')
            else:
                return render(request, "Guest/Shop.html", {"district": dis, "error": "Sign-up failed."})

        except Exception as e:
            return render(request, "Guest/Shop.html", {"district": dis, "error": "An error occurred during sign-up."})
    return render(request, "Guest/Shop.html", {"district": dis})




def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        auth_response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password,
        })
        if auth_response.user:
            user_data = auth_response.user
            user_id = user_data.id
            try:
                user = tbl_user.objects.get(user_id=user_id)
                request.session['uid'] = user.user_id
                return redirect('User:homepage')
            except tbl_user.DoesNotExist:
                try:
                    shop_user = tbl_shop.objects.get(shop_id=user_id)
                    request.session['sid'] = shop_user.shop_id
                    return redirect('Shop:homepage')

                except tbl_shop.DoesNotExist:
                    return render(request, 'Guest/Login.html', {'error': 'User not found'})
        return render(request, 'Guest/Login.html')
    else:
        return render(request, "Guest/Login.html")
