from django import forms
from .models import Post, Comment

# 게시글 작성 폼
class PostForm(forms.ModelForm):

    class Meta:
        model = Post # 폼에서 사용할 모델 지정
        fields = ('title', 'text',) # 폼 필드 2개 생성


# 댓글 작성 폼
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = ('author', 'text',)
        fields = ('text',)
        # fields 에는 모델에 정의된 컬럼만 사용가능


