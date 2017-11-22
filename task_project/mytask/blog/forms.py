from django import forms
from django.contrib.auth.models import User
from blog.models import Post, Comment, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput()
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'country', 'city')

        widgets = {
        'birth_date': forms.DateInput(format='%d/%m/%Y'),
        'country': forms.TextInput(),
        'city': forms.TextInput()
        }


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ("author", "title", "text")

        widgets = {
            "title": forms.TextInput(attrs = {"class": "textinputclass"}),
            "text": forms.Textarea(attrs={"class": "postcontent"})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ("author", "text")

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea()
        }
