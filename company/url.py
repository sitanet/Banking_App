from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from financelens import settings
from company import views


urlpatterns = [
   
   #Admin
    path('company/',views.company, name="company"),


  
   
]+static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)