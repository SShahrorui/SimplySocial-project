from django.contrib import admin
from socialApp.models import Profile,Post,Reply,Likes,Follow,Settings,Privacy
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Likes)
admin.site.register(Follow)
admin.site.register(Settings)
admin.site.register(Privacy)
