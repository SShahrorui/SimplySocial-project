from django import forms
from django.contrib.auth.forms import User,UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
#from socialApp.models import
from django.forms import ModelForm

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
