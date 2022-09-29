from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm


# 유저가 작성하려는 양식을 장고 폼으로 만든다.
# 빈 양식을 만들어서 html로 내보낸다.
def post(request):

    # print('\n\n\n')
    # print(request.method) # GET 인지 POST 인지 출력해준다.
    # # GET : 사이트 접속
    # # POST : 사이트에 입력하고 확인 누르면 나오더라 - 유저 입력 정보
    # print('\n\n\n')

    # form = PostForm() # 상단 from .forms import PostForm 추가
    # return render(request, "lotto/form.html", {"form": form})

    if request.method == "POST":
        # print(request.POST) # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # print(request.method) # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # 사용자로부터 넘겨져 온 POST 요청 데이터를 담아 PostForm 객체 생성
        form = PostForm(request.POST) # filled form
        # print(type(form)) # <class 'lotto.forms.PostForm'>
        # print(form)

        # 채워진 것들로 문제가 없는지 봄. name은 문자여야하고 등등 - models.에 있는거.
        # bool 값으로 준다.
        if form.is_valid():
	    # 사용자로부터 입력받은 form 데이터에서 추가로 수정해주려는 사항이 있을 경우 save를 보류함

            # 하나의 행에 대해서 save 실행하면, db에 저장된다.
            # commit=True면 확정적으로 db에 저장이다. 이게 default값.
            # false면 일단 db에 저장은 안함.
            # 중간저장한 행을 주고, lotto에 저장한다.
            '''
            lotto.text = lotto.text.upper()
            lotto.lottos = '[1, 2, 3, 44, 55, 66]'
            lotto.save()
            이렇게 써도 된다.
            '''
            lotto = form.save(commit = False) # 최종 DB 저장은 아래 generate 함수 내부의 .save()로 처리
            print(type(lotto)) # <class 'lotto.models.GuessNumbers'>
            print(lotto)

            # 제너레이트 실행하면, 로또번호 생성되고 lotto 생기고
            # 현재시간 나오고, 저장된다. - 기능 이미 있음. models.py 봐라.
            lotto.generate()
            # 리다이렉트 : 특정한 url로 가거라~ 하는 것.
            # url 패턴의 별명을 써주면 된다.
            # path('lotto/', views.index, name='index')

            return redirect('index') # urls.py의 name='index'에 해당
            # -> 상단 from django.shortcuts import render, redirect 수정
    # 없으면 돌아가~
    else:
        form = PostForm() # empty form
        return render(request, "lotto/form.html", {"form": form})



# # Create your views here.
# def index(request): # 반드시 먼저 써줘야 한다. 모든 함수에 첫 번째로 써줘야 한다. hp?t? 요청을 통째로 넘겨줌
#     # 1.유저의 요청 2.어떤 html파일을 유저에게 줄 것인지 3.dict : html에 예측 결과를 꽂아서 유저에게 보내줌
#     return render(request, 'lotto/default.html', {})
#     # views 함수에서 retrun은 html 파일이다.


def index(request):
    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온다. name~update_date
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음
    return render(request, 'lotto/default.html', {'lottos':lottos}) # context-dict
    # 리스트 형식으로 관리자 페이지에서 넣은 1번째와 쉘에서 추가한 2번째가 나옴
    # 즉, db에 있는게 나옴



def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


# id를 받아서, 페이지를 보게 해줌.
def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key
    return render(request, "lotto/detail.html", {"lotto": lotto})
    # lotto 라는 키 값으로 lotto/detail.html 보여줌.


