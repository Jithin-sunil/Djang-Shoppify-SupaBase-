from django.shortcuts import render,redirect
from Admin.models import *

# Create your views here.

def district(request):
    district_data = tbl_district.objects.all()
    if request.method == 'POST':
        district_name = request.POST.get('txt_dis')
        if district_name:
            tbl_district.objects.create(district_name=district_name)
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/District.html', {'district': district_data})

def deldistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district")

def editdistrict(request,id):
    district_data = tbl_district.objects.get(id=id)
    if request.method == 'POST':
        district_name = request.POST.get('txt_dis')
        tbl_district.objects.filter(id=id).update(district_name=district_name)
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/District.html', {'edit': district_data})

def place(request):
    dis=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method == 'POST':
        district_id = request.POST.get('sel_district')
        place_name = request.POST.get('txt_place')
        tbl_place.objects.create(place_name=place_name, district=tbl_district.objects.get(id=district_id))
        return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html', {'district': dis, 'place': place})


def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")

def editplace(request,id):
    dis=tbl_district.objects.all()
    place_data = tbl_place.objects.get(id=id)
    if request.method == 'POST':
        district_id = request.POST.get('sel_district')
        place_name = request.POST.get('txt_place')
        tbl_place.objects.filter(id=id).update(place_name=place_name, district=tbl_district.objects.get(id=district_id))
        return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html', {'district': dis, 'edit': place_data})




def category(request):
    category_data = tbl_category.objects.all()
    if request.method == 'POST':
        category_name = request.POST.get('txt_dis')
        if category_name:
            tbl_category.objects.create(category_name=category_name)
        return redirect("Admin:category")
    else:
        return render(request, 'Admin/Category.html', {'category': category_data})

def delcategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:category")

def editcategory(request,id):
    category_data = tbl_category.objects.get(id=id)
    if request.method == 'POST':
        category_name = request.POST.get('txt_dis')
        tbl_category.objects.filter(id=id).update(category_name=category_name)
        return redirect("Admin:category")
    else:
        return render(request, 'Admin/Category.html', {'edit': category_data})



def subcategory(request):
    dis=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method == 'POST':
        category_id = request.POST.get('sel_category')
        subcategory_name = request.POST.get('txt_subcategory')
        tbl_subcategory.objects.create(subcategory_name=subcategory_name, category=tbl_category.objects.get(id=category_id))
        return redirect("Admin:subcategory")
    else:
        return render(request, 'Admin/subcategory.html', {'category': dis, 'subcategory': subcategory})


def delsubcategory(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory")

def editsubcategory(request,id):
    dis=tbl_category.objects.all()
    subcategory_data = tbl_subcategory.objects.get(id=id)
    if request.method == 'POST':
        category_id = request.POST.get('sel_category')
        subcategory_name = request.POST.get('txt_subcategory')
        tbl_subcategory.objects.filter(id=id).update(subcategory_name=subcategory_name, category=tbl_category.objects.get(id=category_id))
        return redirect("Admin:subcategory")
    else:
        return render(request, 'Admin/subcategory.html', {'category': dis, 'edit': subcategory_data})