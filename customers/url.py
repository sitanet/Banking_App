from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from financelens import settings
from customers import views


urlpatterns = [
   
   #Admin
    path('new_account/',views.new_account, name="new_account"),


  
   
]+static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)