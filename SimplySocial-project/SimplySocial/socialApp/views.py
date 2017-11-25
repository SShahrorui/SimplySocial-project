from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from socialApp.forms import SignUpForm,LoginForm


# Create your views here.
def JoinSignupLogin(request):
    signup_form = SignUpForm()
    login_form = LoginForm()
    if request.method == 'POST' and  request.POST.get('submit') == 'signin':
        login_form = LoginForm(data=request.POST)
        #if request.POST.get('submit') == 'signin':
        print('in login form')
        # your sign in logic goes here
        if login_form.is_valid():
            print('valid login form')
            username =  login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('socialApp:home')

    elif request.method == 'POST' and request.POST.get('submit') == 'signup':
            signup_form = SignUpForm(request.POST)
            print('in sign')
            # your sign up logic goes here
            if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                raw_password = signup_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('socialApp:home')
    else:
        signup_form = SignUpForm()
        login_form = LoginForm()
    return render(request, 'socialApp/signup.html', {'login_form':login_form,'signup_form': signup_form})


@login_required
def home(request):
    return render(request, 'socialApp/home.html')
