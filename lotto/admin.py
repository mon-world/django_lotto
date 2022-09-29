from django.contrib import admin

# from lotto.models import GuessNumbers
from .models import GuessNumbers # 자기자신이 속해있는 것이면 이렇게 써도 괜찮다.

# Register your models here.
admin.site.register(GuessNumbers)   # GuessNumbers를 관리자 페이지에 등록.
