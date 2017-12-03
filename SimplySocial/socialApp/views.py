from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from socialApp.models import Post,Profile
from socialApp.forms import SignUpForm,LoginForm,PostForm,ProfileForm,UserForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import(DetailView)


from django.http import *
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


#from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.generic import(TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)



# Create your views here.

#signup/signin

def JoinSignupLogin(request):
    signup_form = SignUpForm()
    login_form = LoginForm()
    profile = Profile()

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
                if user.is_authenticated():
                    profile.user = User(request.user.id)
                    profile.profile_pic= 'profile_pic/index.png'
                    profile.save()
                return redirect('socialApp:home')

    else:
        signup_form = SignUpForm()
        login_form = LoginForm()
    return render(request, 'socialApp/signup.html', {'login_form':login_form,'signup_form': signup_form})

#postfeed/postform
@login_required
def home(request):
    post_form = PostForm()
    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post_form.instance.user = User(current_user.id)
            post_form.instance.user_profile = Profile.objects.get(user=current_user)
            print(request.FILES)
            if "image" in request.FILES:
                post.image = request.FILES['image']
            post.save()
            post_form = PostForm()

    else:
        post_form = PostForm()

    #loadmore
    old_posts = Post.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(old_posts, 1)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'socialApp/home.html',{'post_form':post_form,'posts':numbers})

#postfeed/grid view
@login_required
def home_grid(request):
    post_form = PostForm()
    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post_form.instance.user = User(current_user.id)
            post_form.instance.user_profile = Profile.objects.get(user=current_user)
            print(request.FILES)
            if "image" in request.FILES:
                post.image = request.FILES['image']
            post.save()
            post_form = PostForm()

    else:
        post_form = PostForm()

    #loadmore
    old_posts = Post.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(old_posts, 3)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'socialApp/home-grid.html',{'post_form':post_form,'posts':numbers})

#posts with photo
@login_required
def photos(request):
    post_form = PostForm()
    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post_form.instance.user = User(current_user.id)
            post_form.instance.user_profile = Profile.objects.get(user=current_user)
            print(request.FILES)
            if "image" in request.FILES:
                post.image = request.FILES['image']
            post.save()
            post_form = PostForm()

    else:
        post_form = PostForm()
    old_posts = Post.objects.filter(~Q(image='null')).order_by('-created_date')
    print(old_posts)
    return render(request, 'socialApp/photos.html',{'post_form':post_form,'posts':old_posts})

#posts with video
@login_required
def videos(request):
    post_form = PostForm()
    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post_form.instance.user = User(current_user.id)
            post_form.instance.user_profile = Profile.objects.get(user=current_user)
            print(request.FILES)
            if "image" in request.FILES:
                post.image = request.FILES['image']
            post.save()
            post_form = PostForm()

    else:
        post_form = PostForm()
    old_posts = Post.objects.all().order_by('-created_date')
    print(old_posts)
    return render(request, 'socialApp/videos.html',{'post_form':post_form,'posts':old_posts})

#settings
def profile_update(request,id=None):
    user_form=UserForm()
    profile_form=ProfileForm()
    user_instance=get_object_or_404(User,id=request.user.id)
    print(user_instance)
    profile_instance=get_object_or_404(Profile,id=request.user.id)
    print(profile_instance)
    user_form=UserForm(request.POST,user_instance=user_instance)
    profile_form=ProfileForm(request.POST,profile_instance=profile_instance)
    if user_form.is_valid() and profile_form.is_valid():

        user_instance=user_form.save(commit=False)
        profile_instance=profile_form.save(commit=False)
        user_instance.save()
        profile_instance.save()
        return HttpResponseRedirect("socialApp/SaveSettings.html")
    context={
    "user_instance":user_instance,
    "profile_instance":profile_instance,
    "username":user_instance.username,
    "email":user_instance.email,
    "password":user_instance.password,
    "bio":profile_instance.bio,
    "website":profile_instance.website,
    "profile_form":profile_form,
    "user_form":user_form,
    }

    return render(request,"socialApp/SaveSettings.html",context)

#Search function
def search (request):
   if request.method =='POST':
       srch = request.POST['srh']

       if srch:

           match = User.objects.filter(Q(username__icontains=srch) |Q(email__icontains=srch) )
           print(match)
           if match:
               return render(request, 'socialApp/result.html', {'match':match})
           else:
               messages.error(request,'no result found')

       else:
           return HttpResponseRedirect ('socialApp:search')

   return render(request,'socialApp/result.html')

def user_detail(request,username):
    
    try:
        user = User.objects.filter(username=username)
        post = Post.objects.filter(user=user)
    except User.DoesNotExist:
       raise Http404

    return render(request,'socialApp/profile.html',{'user':user,'posts':post})
