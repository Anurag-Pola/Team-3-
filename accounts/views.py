from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import FpoSignUpForm, DealerSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def register(request):
    return render(request, 'accounts/register.html')

class fpo_register(CreateView):
    model = User
    form_class = FpoSignUpForm
    template_name = 'accounts/fpo_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('fpo:index_fpo')

class dealer_register(CreateView):
    model = User
    form_class = DealerSignUpForm
    template_name = 'accounts/dealer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dealer:index_dealer')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                if user.is_fpo==True:
                    return redirect('fpo:index_fpo')
                else:
                    return redirect('dealer:index_dealer')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'accounts/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('accounts:index')

def index(request):
    return render(request, 'accounts/index.html')