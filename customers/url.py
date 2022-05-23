from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from financelens import settings

from .views import customer_view,list_edit_account


urlpatterns = [
   
   #Admin
    path('new_account/',customer_view, name="new_account"),
    path('list_edit_account/',list_edit_account, name="list_edit_account"),
    path('list_edit_account/<int:cust_no>/',list_edit_account, name='list_edit_account_edit'),
    path('list_edit_account/<int:cust_no>/',list_edit_account, name='list_edit_account_delete'),

    
   
   
   



  
   
]+static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)