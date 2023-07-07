from django import forms
from .models import Post

class FormUpdatePost(forms.Form):
    class Meta:
        model = Post
        fields = ('body',)