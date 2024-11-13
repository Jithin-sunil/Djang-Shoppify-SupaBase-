from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns=[
    
    path('district/',views.district,name="district"),
    path('deldistrict/<int:id>',views.deldistrict,name="deldistrict"),
    path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),

    path('place/',views.place,name="place"),
    path('delplace/<int:id>',views.delplace,name="delplace"),
    path('editplace/<int:id>',views.editplace,name="editplace"),

    path('category/',views.category,name="category"),
    path('delcategory/<int:id>',views.delcategory,name="delcategory"),
    path('editcategory/<int:id>',views.editcategory,name="editcategory"),


    path('subcategory/',views.subcategory,name="subcategory"),
    path('delsubcategory/<int:id>',views.delsubcategory,name="delsubcategory"),
    path('editsubcategory/<int:id>',views.editsubcategory,name="editsubcategory"),
]