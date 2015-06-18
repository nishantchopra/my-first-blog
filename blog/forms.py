from django import forms
from .models import Post
from .models import login

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)

class loginForm(forms.ModelForm):
	class Meta:
		model = login
		fields = ('username','password',)



