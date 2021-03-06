""" Create Blog Posts"""
from django import forms
from .models import Post


class BlogForm(forms.ModelForm):
    """ Form to create blog posts"""
    class Meta:

        model = Post
        fields = ('title', 'body', 'created_by', 'image_url', 'image')
