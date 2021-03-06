from django.urls import path
from . import views
from django.conf.urls import url

# urls.py 에서는 views.py 호출하여 웹에서의 path(path함수 첫 인자)에 render 할 html 템플릿을 찾음
# path(웹에서 보여지는 URL, html을 URL에 맵핑하기 위해 호출할 함수, a 태그 url과 매핑할 속성)

urlpatterns = [
    path('', views.post_list, name='post_list'), # 127.0.0.1:8080 접속 시 
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # path('웹에서의 path', views.py 내 post_detail() 찾아감, <a href="{% url 'post_detail' pk=post.pk %}">)
    path('post/new', views.post_new, name='post_new'), # 새 글 작성 # views.py post_new() 호출 # 화면에서 a 태그에 url 'post_new'를 지정했기 때문에 name='post_new' 을 보고 찾아옴
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), # 글 수정 # views.py post_edit(request, pk) 2 인자를 넣어 호출
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'), # 임시저장
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'), # 글 게시
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'), # 글 삭제
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'), # 댓글 쓰기
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
