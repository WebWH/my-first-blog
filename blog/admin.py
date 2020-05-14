from django.contrib import admin
from .models import Post, Comment

# 관리자 패널에 모델 등록
admin.site.register(Post) # 게시글
admin.site.register(Comment) # 댓글
