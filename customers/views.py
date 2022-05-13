from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
from django.contrib import messages
from django.contrib import messages
from django.db import transaction
from django.core.paginator import Paginator




# Create your views here.

def new_account(request):
    return render(request, "customer/new_account.html")


# Create your views here.
