from django.shortcuts import render,redirect
from .models import Cake
from .forms import UserRegistrationForm
from .forms import LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,"home.html")

def product(request):
    products = Cake.objects.all()
    return render(request,"product.html",{'products':products})

def single_product(request,pk):
    product=Cake.objects.get(pk=pk)
    products = Cake.objects.filter()[0:4]
    return render(request,"single product.html",{'products':products,'product':product})

def profile(request):

    return render(request,"profile.html")

def contact(request):
    return render(request,"contact.html")

def cart(request):
    return render(request,"cart.html")

def signup(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return redirect('cake:login')
        
    else:
        user_form = UserRegistrationForm()
        
    return render(request,"signup.html", {'user_form': user_form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                emailaddress=cd['emailaddress'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('cake:home')  # Redirect to login page
                else:
                    return render(request,'login.html',{'form': form})
            else:
                return render(request,'login.html',{'form': form})
    else:
        form = LoginForm()
    return render(request,'login.html',{'form': form})