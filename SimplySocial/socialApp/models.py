from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    id =models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    profile_pic= models.ImageField(upload_to = "profile_pic/",default = 'profile_pic/index.png', blank=True, null=True)
    bio=models.CharField(max_length=255)
    website=models.URLField()

    def __str__(self):
        return str(self.user)



class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    text = models.TextField(max_length=140)
    created_date = models.DateTimeField(default=timezone.now)
    modifed_date = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(upload_to="post_pic/",max_length=255, blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.text

class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    text = models.TextField(max_length=140)
    created_date = models.DateTimeField(default=timezone.now)
    modifed_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.text

class Settings(models.Model):
    settings_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email_fav = models.BooleanField()
    email_reply = models.BooleanField()
    email_follow_me = models.BooleanField()


class Privacy(models.Model):
    privacy_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.BooleanField()

class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rel_from_set')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rel_to_set')
    created = models.DateTimeField( db_index=True,default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user, self.following)

User.add_to_class('following',
                             models.ManyToManyField('self',
                                         through=Follow,
                                         related_name='followers',
                                         symmetrical=False))
class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply,on_delete=models.CASCADE,null=True)
    created_date = models.DateTimeField(default=timezone.now)
