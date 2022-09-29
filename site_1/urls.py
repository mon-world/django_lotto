"""site_1 URL Configuration == 세팅

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:

Function views - 가장 많이 활용
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home') # views.함수와 별명

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf (url 권한 위임)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from lotto import views             # 1. 앱 폴더로부터 views 파일을 임포트 한다.
from django.contrib import admin
from django.urls import path

# 페이지 주소 만드는 곳.
# 맨 앞에 메인 url이 생략되어 있다. 로컬에선 127.0.0.1:8000/
# 나중에 배포할 때 다 수정해야 하므로 아무것도 적지 말자. - 장고에서 지원해줌
urlpatterns = [
    path('admin/', admin.site.urls),    # admin.site.urls에 권한위임중 - 관리자 만들면 sql에 저장됨.
    # path('', views.index),              # 2. lotto > views.py 파일의 index() 함수 호출 - 보통 이 이름 씀
                                        # views의 index 함수에 ''안의 url을 넘겨주라는 뜻
    path('hello/', views.hello, name='hello_name'),
    path('lotto/', views.index, name='index'),          # http://127.0.0.1:8000/lotto/
    path('lotto/new', views.post, name = "new_lotto"),
    path('lotto/<int:lottokey>/detail', views.detail, name='detail'),   # id 번호로 보여주기
]
