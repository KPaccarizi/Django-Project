from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, User
from django import forms
from django import forms
from .models import Document
from .models import BlogPost




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('docfile',)
        widgets = {
            'docfile': forms.ClearableFileInput(attrs={'multiple': True, 'accept': 'image/*'}),
        }


class BlogPostForm(forms.ModelForm):
    upload = forms.FileField(required=False, label='Upload File')  # Add this line

    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'content', 'upload']



class SearchForm(forms.Form):
    query = forms.CharField()


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, help_text="Required.")
    email = forms.EmailField(max_length=254, required=True, help_text="Required.")
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Required.")
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
