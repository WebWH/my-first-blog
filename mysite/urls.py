"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('blog.urls')), # 127.0.0.1:8080 접속 시 C:\django\blog\urls.py 찾아간 다음 path('', views.post_list, name='post_list'), 에 의해 post_list.html 응답
    url(r'^admin/', admin.site.urls), # 사용자 로그인
    url(r'^accounts/login/$', views.login, name='login'), # 사용자 로그인
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}), # 로그아웃
    url(r'', include('blog.urls')), # 사용자 로그인
]
