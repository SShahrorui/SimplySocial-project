from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from socialApp.models import Post,Profile,Reply,Likes,Follow
from socialApp.forms import SignUpForm,LoginForm,PostForm,ProfileForm,UserForm,ReplyForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import(DetailView)
from django.urls import reverse

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
            if user.is_authenticated():
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
    user_list = {}
    post_list = {}
    #loadmore
    follow = Follow.objects.filter(user=current_user)
    old_posts = Post.objects.all().order_by('-created_date')

    #for user in follow:
        #user_follow = User.objects.filter(id=user.following.id)
        #user_list[user]=user_follow
    #for post in old_posts:
        #post_list[post] =

    replys = Reply.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(old_posts, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'socialApp/home.html',{'post_form':post_form,'posts':numbers,'replys':replys,'follow':follow})

@login_required
def post_reply(request,pk):
    # List of active comments for this post
    reply_form = ReplyForm()
    current_user = request.user
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply=reply_form.save(commit=False)
            reply_form.instance.user = User(current_user.id)
            reply_form.instance.user_profile = Profile.objects.get(user=current_user)
            reply_form.instance.post = Post.objects.get(post_id=pk)
            reply.save()
            reply_form = ReplyForm()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
            reply_form = ReplyForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



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
    follow = Follow.objects.filter(user=current_user)
    old_posts = Post.objects.all().order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(old_posts, 3)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'socialApp/home-grid.html',{'post_form':post_form,'posts':numbers,'follow':follow})

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
    follow = Follow.objects.filter(user=current_user)
    old_posts = Post.objects.filter(~Q(image='null')).order_by('-created_date')
    print(old_posts)
    return render(request, 'socialApp/photos.html',{'post_form':post_form,'posts':old_posts,'follow':follow})

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
    follow = Follow.objects.filter(user=current_user)
    old_posts = Post.objects.all().order_by('-created_date')
    print(old_posts)
    return render(request, 'socialApp/videos.html',{'post_form':post_form,'posts':old_posts,'follow':follow})

#settings
def profile_update(request,id=None):

    instance_user=get_object_or_404(User,id=id)
    username = instance_user.username
    print(username)
    instance_profile=get_object_or_404(Profile,user=instance_user)
    print(instance_profile)
    user_form=UserForm(request.POST or None,instance=instance_user)
    profile_form=ProfileForm(request.POST,instance=instance_profile)

    if user_form.is_valid():
        instance_user = user_form.save(commit=False)
        instance_user.save()

    if profile_form.is_valid():
        instance_profile = profile_form.save(commit=False)
        print(request.FILES)
        if "profile_pic" in request.FILES:
            instance_profile.profile_pic = request.FILES['profile_pic']
            instance=instance_profile

        instance_profile.save()

    context={
    "username":instance_user.username,
    "email":instance_user.email,
    "password":instance_user.password,
    "bio":instance_profile.bio,
    "website":instance_profile.website,
    "profile_pic":instance_profile.profile_pic,
    "instance_user":instance_user,
    "instance_profile":instance_profile,
    "user_form":user_form,
    "profile_form":profile_form,
    }

    return render(request,"socialApp/settings.html",context)

#Search function
def search (request):
   if request.method =='POST':
       srch = request.POST['srh']

       if srch:

           match = User.objects.filter(Q(username__icontains=srch) |Q(email__icontains=srch) )
           profile = Profile.objects.filter(user=match)
           if match:
               return render(request, 'socialApp/result.html', {'match':match,'profile':profile})
           else:
               messages.error(request,'no result found')

       else:
           return HttpResponseRedirect ('socialApp:search')

   return render(request,'socialApp/result.html')

def user_detail(request,username):

    try:
        user = User.objects.filter(username=username)
        post = Post.objects.filter(user=user)
        profile = Profile.objects.filter(user=user)
        follow = Follow.objects.filter(user=request.user,following=user)
        print(follow)
    except User.DoesNotExist:
       raise Http404

    return render(request,'socialApp/profile.html',{'user':user,'posts':post,'profile':profile,'follow':follow})

def like(request,pk):
    print('in like')
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    print(user)
    liked_post = Post.objects.get(post_id=pk)
    print (liked_post)

    post_likes = Likes.objects.filter(user= user,post=liked_post)

    if post_likes.exists():
        post_likes.delete()
        post_likes.save()

    else:
        new_like = Likes()
        new_like.user = current_user
        new_like.post = liked_post
        new_like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def follow(request,pk):

    print('in follow')
    current_user = request.user
    follow_sender = User.objects.get(id=current_user.id)
    follow_receiver = User.objects.get(id=pk)
    follow_flag = False
    if (follow_sender==follow_receiver):
        print('user can not follow himself!')
    else:
        follow_request = Follow.objects.filter(user=follow_sender,following=follow_receiver)

        if follow_request.exists():
            print('already a follower')
            follow_request.delete()
            follow_request.update()
            follow_flag = False
        else:
            new_request = Follow()
            new_request.user = follow_sender
            new_request.following =follow_receiver
            print(new_request)
            new_request.save()
            follow_flag = True

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def get_user_followers(request):

    current_user = request.user
    followers = Follow.objects.filter(following=current_user)
    user = User.objects.filter(id=current_user.id)
    profile = Profile.objects.all()
    print(followers)

    return render(request,'socialApp/followers.html',{'followers':followers,'profile':profile,'user':user})

@login_required
def get_user_following(request):

    current_user = request.user
    following = Follow.objects.filter(user=current_user)
    user = User.objects.filter(id=current_user.id)
    profile = Profile.objects.all()
    print(following)
    return render(request,'socialApp/following.html',{'following':following,'profile':profile,'user':user})

def get_user_likes(request):

    current_user=request.user
    user = User.objects.filter(id=current_user.id)
    profile = Profile.objects.filter(user=user)
    print(user)
    likes = Likes.objects.filter(user=current_user)
    post = Post.objects.all().order_by('-created_date')
    return render(request,'socialApp/likes.html',{'likes':likes,'posts':post,'user':user,'profile':profile})
