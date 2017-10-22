from django.conf.urls import url
from userApp import views

#Template urls
app_name='userApp'

urlpatterns=[
    url(r'^register/$',views.register,name="register"),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
