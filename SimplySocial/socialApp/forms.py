from django import forms
from django.contrib.auth.forms import User,UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from socialApp.models import Post,Profile
from django.forms import ModelForm
#from django.contrib.auth import get_user_model

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Browse',
    )


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254,
                                widget=forms.EmailInput(attrs={'placeholder': 'Email'}) )
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username':forms.TextInput(attrs={'placeholder': 'User Name'}),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email is already used")
        return data

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        fields = ('username','password')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text','image','video_link')
        widgets = {
            'text':forms.TextInput(attrs={'placeholder': 'Whats in your mind?','class':"postArea col-lg-12"}),
            'image':forms.FileInput(attrs={'class':'browse','id':'image' }),
            'video_link':forms.URLInput(attrs={'class':'video-box','id':'linkBox'})
        }
    '''
    def clean(self):
        data = self.cleaned_data
        if  not (Post.image==None and Post.video_link==None):
            raise forms.ValidationError("Attach either photo or video.")
        return data
    '''


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_pic','bio','website')





class UserForm(forms.ModelForm):
   class Meta:
       model = User
       fields = ('username', 'email', 'password')
