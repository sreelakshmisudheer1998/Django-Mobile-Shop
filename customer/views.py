from django.shortcuts import render
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login as django,logout


# Create your views here.
def index(request):
    return render(request,"index.html")

def registration(request,*args,**kwargs):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    return render(request,"registration.html",context)

def login_view(request,*args,**kwargs):
    form=LoginForm()

def sign_out(request,*args,**kwargs):
    form=LoginForm()
    context={}
    context["form"]=form
    # if request.method == "POST":
    #     form=LoginForm(request.POST)
    #     if form.is_valid():




