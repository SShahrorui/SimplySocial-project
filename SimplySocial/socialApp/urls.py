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
url(r'^(?P<id>\d+)/edit/$',views.profile_update,name="SettingsUpdate"),
url(r'^search/result/$',views.search,name="search"),
url(r'^(?P<username>\w+)/profile/$',views.user_detail,name="profile"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
