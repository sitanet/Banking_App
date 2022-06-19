from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from financelens import settings

from .views import customer_view,list_edit_account,cust_edit,customer_delete


urlpatterns = [
   
   #Admin
    path('new_account/',customer_view, name="new_account"),
    path('list_edit_account/',list_edit_account, name="list_edit_account"),
    path('new_account/<int:cust_no>/',cust_edit, name='edit_customer'),
    path('customer_delete/<int:cust_no>/',customer_delete, name='delete'),

    
   
   
   



  
   
]+static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)