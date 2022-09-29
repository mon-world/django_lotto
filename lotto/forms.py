# 유저에게 입력을 받는 기능 수행
from django import forms
from .models import GuessNumbers

# Django에서 제공하는 ModelForm을 활용해 form 구성
# form 태그 직접 작성할 필요 없이 알아서 만들어준대!
class PostForm(forms.ModelForm):

    # Form을 통해 받아들여야할 데이터가 명시되어 있는 메타 데이터 (DB 테이블을 연결)
    # 메타 : 상위의 라는 뜻
    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',) # 사용자로부터 form 통해 입력받을 데이터
        # 알아서 name하고 text 찾아서 입력해준다. 왜 이렇게 쓰는거지???
