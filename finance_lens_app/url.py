from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
import customers
from financelens import settings
from finance_lens_app import admin_views



urlpatterns = [
    path('',admin_views.home, name="home"),
   #Admin
    path('login/',admin_views.loginPage, name="loginPage"),
    path('logout/',admin_views.logout_page, name="logout"),
 
    path('acct_settings/',admin_views.acct_settings, name="acct_settings"),
    path('coa/',admin_views.coa_view, name='coa'),
    path('coa_edit/<int:id>/',admin_views.coa_edit, name='coa_edit'),
    path('coa_delete/<int:id>/',admin_views.coa_delete, name='coa-delete'),
    path('acct_type/',admin_views.acct_type, name="acct_type"),
    path('acct_type/',admin_views.acct_type, name="acct_type"),
    path('acct_cat/',admin_views.acct_cat, name="acct_cat"),
    path('', include('customers.url')),
    path('', include('employee.url')),
    path('', include('company.url')),

   

  
   
]+static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)