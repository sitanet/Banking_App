from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from customers.models import Customer
from company.models import Company
from finance_lens_app.models import coa
from .forms import customers
from django.contrib import messages
from .filters import CustomerFilter


# Create your views here.

def customer_view(request):
 
    # create object of form
    if request.method == 'POST':
        form = customers(request.POST, request.FILES)
   
    # check if form data is valid
        if form.is_valid():
        
        # save the form data to model
            form.save()
            LastInsertId = (Customer.objects.last()).cust_no
            name = (Customer.objects.last()).name
            messages.success(request, 'Welcome ' + str(name )+' Your Account No is ' + str(LastInsertId))
            return redirect('new_account')
    else:
        form = customers()
  
      
    return render(request, "customer/new_account.html", {"form":form})
  


# For displaying the Edit Form.
def list_edit_account(request):
    if request.method=="GET":
        cust_info=Customer.objects.all()
        cust_info2=CustomerFilter(request.GET, queryset=cust_info)
        cust_info=cust_info2.qs
        
        paginator=Paginator(cust_info,10)
        page=request.GET.get('page')
        cust_info=paginator.get_page(page)
        return render(request, "customer/list_edit_account.html",{"cust_info2":cust_info2,"cust_info":cust_info})
   

# For display a customer form to edit.
def cust_edit(request, cust_no):
        cust_id =Customer.objects.get(cust_no=cust_no)
        if request.method == 'POST':
            form = customers(request.POST or None, instance=cust_id)
            if form.is_valid():
                form.save()
                messages.success(request,'Account Updated Successfully...')
                return redirect('list_edit_account')
            
        else:
            cust_id =Customer.objects.get(cust_no=cust_no)
            form = customers(request.POST or None, instance=cust_id)
      
            Comp_data=Company.objects.all()
            cust_data=Customer.objects.all()
            coa_data=coa.objects.all()

            cust_id =Customer.objects.get(cust_no=cust_no)
            context = {"cust_id":cust_id,"Comp_data":Comp_data,"cust_data":cust_data,"coa_data":coa_data,"form":form,}
            return render(request, "customer/new_account.html", context)



def customer_delete(request, cust_no):
        cust_del =Customer.objects.get(cust_no=cust_no)
        if request.method == 'POST':
            cust_del.delete()
            messages.success(request,'Account Deleted Successfully...')
            return redirect('list_edit_account')
        return render(request, "customer/customer_delete.html",{'cust_del': cust_del})

# Create your views here.
