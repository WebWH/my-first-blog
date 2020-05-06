from django.urls import path
from . import views

# urls.py 에서는 views.py 호출하여 웹에서의 path(path함수 첫 인자)에 render 할 html 템플릿을 찾음

urlpatterns = [
    path('', views.post_list, name='post_list'), # 127.0.0.1:8080 접속 시 
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # path('웹에서의 path', views.py 내 post_detail() 찾아감, <a href="{% url 'post_detail' pk=post.pk %}">)
    path('post/new', views.post_new, name='post_new'), # 새 글 작성
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # 글 수정
]