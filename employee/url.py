from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from financelens import settings
from customers import views


urlpatterns = [
   
   #Admin
    path('employee/',views.new_account, name="employee"),


  
   
]+static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)