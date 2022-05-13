from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Acct_type, acct_head, coa
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_auth, logout
from django.contrib.auth.decorators import login_required
from .forms import Acct_type_form,Acct_head_form
from django.contrib import messages
from django.db import transaction
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, "admin/home.html")




def loginPage(request):
    return render(request, "login.html")



def logout_page(request):
    logout(request)
    return redirect('loginPage')

def acct_settings(request):
    return render(request, "admin_opera/acct_settings.html")




def coa_view(request):
    if request.method =='POST':
        ac_type =request.POST.get('ac_type')
        ac_head =request.POST.get('ac_head')
        ac_name =request.POST.get('ac_name')
        gl_no =request.POST.get('gl_no')
        currcy =request.POST.get('currcy')

        
        if (ac_head!=gl_no[0]):
            messages.warning(request, 'Account Name is Not in the Proper Heading!')
            return redirect('coa')

        if coa.objects.filter(ac_name=ac_name).exists():
            messages.warning(request, 'Account Name is Existing!')
            return redirect('coa')

        
        if coa.objects.filter(gl_no=gl_no).exists():
             messages.warning(request, 'General Ledger No. is Existing!')
             return redirect('coa')

       
        
        else:
            record2 = coa(ac_type=ac_type,ac_head=ac_head,ac_name=ac_name,gl_no=gl_no,currcy=currcy)
            record2.save()
            messages.success(request,'Account Type Added Successfully...')
    else:
        pass
    acct_type_data=Acct_type.objects.all().order_by('Aid')
    acct_cat_data=acct_head.objects.all()
    ac_coa=coa.objects.all().order_by('ac_type').order_by('gl_no')
    paginator=Paginator(ac_coa,5)
    page=request.GET.get('page')
    ac_coa=paginator.get_page(page)

    return render(request, "admin_opera/coa.html", {"type":acct_type_data, "cat":acct_cat_data, "ac_coa":ac_coa})


def coa_edit(request, id):
    if request.method =='POST':
        coa_id =coa.objects.get(id=id)
        coa_id.ac_type =request.POST['ac_type']
        coa_id.ac_head =request.POST['ac_head']
        coa_id.ac_name =request.POST['ac_name']
        coa_id.gl_no =request.POST['gl_no']
        coa_id.currcy =request.POST['currcy']
        coa_id.save()
        messages.success(request,'Account Updated Successfully...')
        return redirect('coa')

    else:

        coa_id =coa.objects.get(id=id)
    acct_type_data=Acct_type.objects.all().order_by('Aid')
    acct_cat_data=acct_head.objects.all()
    ac_coa=coa.objects.all().order_by('ac_type').order_by('gl_no')
    context = {"coa":coa_id,"type":acct_type_data, "cat":acct_cat_data, "ac_coa":ac_coa,}


    
    return render(request, "admin_opera/coa.html", context)



def coa_delete(request, id):
    coa_del =coa.objects.get(id=id)
    if request.method == 'POST':
    
        coa_del.delete()
        messages.success(request,'Account Deleted Successfully...')
    
        return redirect('coa')

    context = {
        'coa_del': coa_del
     }
    return render(request, 'admin_opera/products_delete.html', context)




def acct_type(request):
    if request.method =="POST":
        form = Acct_type_form(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            messages.success(request,'Account Type Added Successfully...')
        
        else:
            messages.success(request, 'Exist...')
            
    form = Acct_type_form()
    
    return render(request, "admin_opera/acct_type.html", {"form":form})
    
     

def acct_cat(request):
   acct_type_data=Acct_type.objects.all().order_by('Aid')
   acct_cat_data=acct_head.objects.all().order_by('gl_no')

   if request.method =="POST":
       with transaction.atomic():
        form = Acct_head_form(request.POST)
        if form.is_valid():
            
            record = form.save(commit=False)
            record.save()
            messages.success(request,'Account Type Added Successfully...')
        else:
            messages.error(request, 'The Account is Existing...')
   form = Acct_head_form()
   return render(request, "admin_opera/acct_cat.html", {"type":acct_type_data, "cat":acct_cat_data})



