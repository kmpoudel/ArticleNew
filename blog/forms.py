from django import forms
from django.forms import ModelForm
from blog.models import Post, Comment

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields= ('title','text','author')

class CommentForm(ModelForm):

	class Meta:
		model = Comment
		fields=('name','email', 'post', 'text')