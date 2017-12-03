from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from socialApp.models import Profile


def userAvatar(request):
    try:
        if request.user.is_authenticated:
            current_user = request.user
            user_avatar = Profile.objects.get(user=current_user)
            return {'user_avatar' : user_avatar}
        else:
            return{}

    except Profile.DoesNotExist:
         return {'user_avatar':''}
