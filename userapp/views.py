from itertools import product
from multiprocessing import context
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from .models import profil
from mainpage.models import Product
from django.contrib.auth.models import User

def register(request):
    if request.method =='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('mainpage:products')

    form=NewUserForm()
    context={
        'form':form 
    }
    return render(request,'register.html',context)
    
@login_required
def profile(request):
    return render(request,'profile.html')

def create_profile(request):
    if request.method =='POST':
        contactnumber=request.POST.get('contactnumber')
        image=request.FILES['upload']
        user= request.user
        Profile1 = profil(user=user,image=image,contact_number=contactnumber)
        Profile1.save()
     
    return render(request,'createprofile.html')

def  seller_profile(request,id):
    seller= User.objects.get(id=id)
    context={
        'seller':seller,
    }
    return render(request,'sellerprofile.html',context)
    

