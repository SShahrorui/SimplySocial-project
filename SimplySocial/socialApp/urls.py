from django.conf.urls import url
from django.contrib.auth import views as auth_views
from socialApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
app_name = 'socialApp'

urlpatterns = [


url(r'^$',views.JoinSignupLogin, name="signup"),
url(r'^home/$',views.home,name="home"),
url(r'^home/grid/$',views.home_grid,name="home_grid"),
url(r'^photos/$',views.photos,name="photos"),
url(r'^videos/$',views.videos,name="videos"),
url(r'^logout/$',auth_views.logout,name="logout",kwargs={'next_page':'/'}),
url(r'^search/result/$',views.search,name="search"),
url(r'^(?P<username>\w+)/profile/$',views.user_detail,name="profile"),
url(r'^post/(?P<pk>\d+)/like/$',views.like,name="like"),
url(r'^(?P<pk>\d+)/follow/$',views.follow,name="follow"),
url(r'^followers/$',views.get_user_followers,name="followers"),
url(r'^following/$',views.get_user_following,name="following"),
url(r'^favourite/$',views.get_user_likes,name="likes"),
url(r'^(?P<id>\d+)/update/$',views.profile_update,name="update"),
url(r'^reply/(?P<pk>\d+)/$',views.post_reply,name="reply"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
