from django.conf import settings
from django.db import models
from django.utils import timezone

# Post는 모델의 이름
# models은 Post가 장고 모델임을 의미합니다. 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


# 댓글
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # created_date = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    approved_comment = models.BooleanField(default=True) # true=> 승인없이 댓글 작성, false=> 댓글 승인 필요

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

# create table
# (myvenv) c:\django> python manage.py makemigrations blog
# (myvenv) c:\django> python manage.py migrate blog
