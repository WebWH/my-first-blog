from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post # 폼에서 사용할 모델 지정
        fields = ('title', 'text',) # 폼 필드 2개 생성