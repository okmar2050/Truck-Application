from django.urls import path
from truckapp import views

urlpatterns = [ 
    path('',views.home_view,name='home'),
    path('truck/',views.truck_view,name='truck'),
    path('truck/add/',views.truck_add_view,name='add'),
    path('truck/update/<pk>',views.truck_update_view,name='update'),
    path('truck/delete/<pk>',views.truck_delete_view,name='delete'),
    path('search/',views.truck_search_view,name='search'),
]
