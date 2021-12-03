from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.urls import reverse_lazy
from django.forms import ModelForm


from django.views.generic import (DetailView, ListView, FormView, CreateView, UpdateView, DeleteView)


# Create your views here.



def bankregister(request):
    if request.method == "POST":
        name = request.POST.get('name')
        id = request.POST.get('id')
        user1 = Bank.objects.filter(name=name, id=id).exists()
        if not user1:
            userpro = Bank.objects.create(
                name=name,
                id=id, 
            )
            userpro.save()
            return render(request, 'bankregister.html', {"msg1": 'Registered successfully'})
        else:
            return render(request, 'bankregister.html', {"msg1": 'Bank already exist'})
        
    else:
        return render(request, 'bankregister.html', {})
def pbankregister(request):
    if request.method == "POST":
        ifsc = request.POST.get('ifsc')
        id = request.POST.get('id')
        address = request.POST.get('address')
        branch = request.POST.get('branch')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        user1 = Public_branches.objects.filter(ifsc=ifsc).exists()
        if not user1:
            userpro = Public_branches.objects.create(
                ifsc=ifsc,
                bank_id=id, 
                branch=branch,
                address=address,
                city=city,
                district=district,
                state=state,
            )
            userpro.save()
            return render(request, 'pbankregister.html', {"msg1": 'Registered successfully'})
        else:
            return render(request, 'pbankregister.html', {"msg1": 'Bank already exist'})
        
    else:
        return render(request, 'pbankregister.html', {})
def pbbankregister(request):
    if request.method == "POST":
        ifsc = request.POST.get('ifsc')
        id = request.POST.get('id')
        address = request.POST.get('address')
        branch = request.POST.get('branch')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        bankname = request.POST.get('bankname')
        
        
        userpro = Public_bank_branches.objects.create(
                ifsc=ifsc,
                bank_id=id, 
                branch=branch,
                address=address,
                city=city,
                district=district,
                state=state,
                bank_name=bankname,
        )
        userpro.save()
        return render(request, 'pbbankregister.html', {"msg1": 'Registered successfully'})
       
    else:
        return render(request, 'pbbankregister.html', {})
def dashboard(request):
    if request.method == "POST":
        print(11111)
        bankname = request.POST.get('bank_name')
        city = request.POST.get('city')
        print(bankname)
        print(city)

        user1=Public_bank_branches.objects.filter(bank_name=bankname,city=city)
        return render(request,"dashboard.html", {'user' : user1})
    else:
       
        user1=Public_bank_branches.objects.all()
        print(user1)
        return render(request,"dashboard.html", {'user' : user1})

      
def bankdashboard(request):
    if request.method == "POST":
        print(11111)
        ifsc = request.POST.get('ifsc')
        
        if ifsc is None:
            user1=Public_branches.objects.all()
            print(user1)
            return render(request,"bankdashboard.html", {'user' : user1})
        else:
            user1=Public_branches.objects.filter(ifsc=ifsc)
            return render(request,"bankdashboard.html", {'user' : user1})
    else:

        user1=Public_branches.objects.all()
        print(user1)
        return render(request,"bankdashboard.html", {'user' : user1})

def test(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Public_bank_branches(bank_name=query) 

            results= Public_bank_branches.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'test.html', context)

        else:
            return render(request, 'test.html')

    else:
        return render(request, 'test.html')
