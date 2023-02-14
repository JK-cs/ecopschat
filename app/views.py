from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404

from app.models import Post


# Create your views here.
def echo_page(request):
 return render(request, "app/echo_page.html")

#Liveblog
#장고 템플릿 렌더링 통해 포스팅 목록을 렌더링
#HTML 페이지 전체를 렌더링
#템플릿 내에서 app/partial/post.html을 활용
#liveblog_index: post 모델에 대한 목록 페이지 구현

def liveblog_index(request:HttpRequest) -> HttpResponse:
 post_list = Post.objects.all()
 return render(request,"app/liveblog_index.html", {
  "post_list": post_list,
 })


#post_partial: 지정 포스트 id의 html만을 렌더링
def post_partial(request: HttpRequest, post_id) -> HttpResponse:
 post = get_object_or_404(Post,pk=post_id)
 return render(request,"app/partial/post.html",{
  "post":post,
 })