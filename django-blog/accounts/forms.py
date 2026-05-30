from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.Form):
    body = forms.CharField(label="Post", widget=forms.Textarea(attrs={"rows": 4}))


class CommentForm(forms.Form):
    text = forms.CharField(label="Comment", max_length=500)


class ProfileSearchForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
