from django.forms import ModelForm
from api.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]
        
    
