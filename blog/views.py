from django.shortcuts import render
from django.utils import timezone # 쿼리셋 정렬에 사용
from .models import Post, Comment # 추가하여 models.py 에 정의된 model 가져오기
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required # 외부인 로그인 글 작성 허가
# 함수 위에 decorator(@login_required) 추가하여 로그인 사용자만 사용할 수 있도록 함

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
@login_required
def post_new(request):
    print("post_new Call !!!!!!")    
    
    # 새 글 작성 버튼을 눌렀을 때에는 request가 없으므로 else로 넘어감
    # form에서 submit하면 현재 URL로 다시 request하므로 여기로 다시옴
    if request.method == "POST":
        form = PostForm(request.POST) # 폼에서 사용자 입력값 가져와서(POST method)
        if form.is_valid(): # 입력값 검증을 함
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now() # 임시저장 기능을 위해 주석
            post.save() # 입력값 저장
            return redirect('post_detail', pk=post.pk) # 상세보기로 화면 전환
    # 새 글 작성 버튼 클릭 시 
    else:
        form = PostForm() # forms.py PostForm class 가져온 다음 post_edit.html에 매핑시킨다.

    return render(request, 'blog/post_edit.html', {'form': form})


# 글 수정
@login_required
def post_edit(request, pk):
    print("post_edit222222222222222222 Call !!!!!!")        
    post = get_object_or_404(Post, pk=pk) # Post 모델 인스턴스 가져오기(pk로 SELECT), 수정을 위해 form에 다시 뿌릴것이기 때문
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # request, 기존 글 내용 Post Model에서 가져오기
        if form.is_valid(): # 입력값 검증
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now() # 임시저장 기능을 위해 주석
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})


# 임시 저장
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


# 게시
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


# 글 삭제
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


# 댓글 쓰기
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# 댓글 승인
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

# 댓글 삭제
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)