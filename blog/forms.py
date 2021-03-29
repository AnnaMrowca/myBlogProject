from blog.models import Post
from django import forms

class  DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'date')
        widgets = {'date': DateInput()}