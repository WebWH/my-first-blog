from django.shortcuts import render
from django.utils import timezone # 쿼리셋 정렬에 사용
from .models import Post # 추가하여 models.py 에 정의된 model 가져오기
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# urls.py 에서 views.py 참조하여 render할 화면 찾음

# 게시판 목록
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # 쿼리셋 정렬
	# posts 은 쿼리셋 이름
    return render(request, 'blog/post_list.html', {'posts': posts}) 
    # C:\django\blog\templates\blog\post_list.html
    # {'posts': posts} : distionary는 템플릿에서 사용할 매개변수

# 게시글 상세보기
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    # C:\django\blog\templates\blog\post_detail.html

# 새 글 작성
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) # 폼에서 사용자 입력값 가져와서(POST method)
        if form.is_valid(): # 입력값 검증을 함
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # 입력값 저장
            return redirect('post_detail', pk=post.pk) # 상세보기로 화면 전환
    else:
        form = PostForm() # forms.py PostForm class
    return render(request, 'blog/post_edit.html', {'form': form})

# 글 수정
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # Post 모델 인스턴스 가져오기(pk로 SELECT), 수정을 위해 form에 다시 뿌릴것이기 때문
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # 기존 글 내용 Post Model에서 가져오기
        if form.is_valid(): # 입력값 검증
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})