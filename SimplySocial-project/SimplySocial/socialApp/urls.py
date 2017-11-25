from django.conf.urls import url
from django.contrib.auth import views as auth_views
from socialApp import views

app_name = 'socialApp'

urlpatterns = [


url(r'^$',views.JoinSignupLogin, name="signup"),
url(r'^home/$',views.home,name="home"),
url(r'^logout/$',auth_views.logout,name="logout",kwargs={'next_page':'/'}),
]
