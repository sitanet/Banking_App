from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect

from customers.models import Customer, coa
from .forms import customers
from django.contrib import messages



# Create your views here.

def customer_view(request):
    context ={}
 
    # create object of form
    form = customers(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        
        # save the form data to model
        form.save()
        LastInsertId = (Customer.objects.last()).cust_no
        name = (Customer.objects.last()).name
        
        

        messages.success(request, 'Welcome ' + str(name )+' Your Account No is ' + str(LastInsertId))
        return redirect('new_account')
   
 
    context['form']= form
    
    return render(request, "customer/new_account.html", context)



def list_edit_account(request):
    cust_info=Customer.objects.all()
    return render(request, "customer/list_edit_account.html",{"cust_info":cust_info})





# Create your views here.
