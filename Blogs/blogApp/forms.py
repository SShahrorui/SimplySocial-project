from django import forms
from blogApp.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields=('auther','title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium_editor_textarea postcontent'})

        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields=('auther','text')

        widgets = {
            'auther':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium_editor_textarea'})

        }
