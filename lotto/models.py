from django.db import models
from django.utils import timezone
import random

# Create your models here.
# 만들 테이블. models.Model을 상속받는다.
# 상속 : 이미 만들어져 있는 설계도(클래스)를 그대로 가져와서, 필요한걸 추가하거나 덮어씀.

# 필드 수정 삭제 변경 할 때마다 해줘야 할 것 : migration 작업 해줘야 한다.
# models.py의 변화를 db schema 즉, db 자체에 반영해주는 과정.
# - python manage.py makemigrations : models.py 에서의 변화를 모아 migration file로 구성 (commit)
# - python manage.py migrate : 구성된 migration file을 바탕으로 실제 DB Schema 변경 (push)

class GuessNumbers(models.Model):
    # CharField : 문자열 쓰겠다는 뜻.
    # db의 필드들의 이름.
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()

    # self : 하나의 객체변수. 붕어빵의 신상정보
    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1,46)) # 1~45의 숫자 리스트 [1, 2, 3, ..., 43, 44, 45]
        # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin) # [10, 21, 36, 2, ... , 1, 11]
            guess = origin[:6] # [10, 21, 36, 2, 15, 23]
            guess.sort() # [2, 10, 15, 21, 23, 36]
            self.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가 -> '[2, 10, 15, 21, 23, 36]\n'
            # self.lottos : '[2, 10, 15, 21, 23, 36]\n[1, 15, 21, 27, 30, 41]\n...'
        self.update_date = timezone.now()
        # self는 클래스의 객체변수 하나.
        # 붕어빵 하나.
        # new_row = GuessNumbers(~~) 이라면 new_row.save() 라는 뜻.
        self.save() # GuessNumbers object를 DB에 저장

    # 객체변수를 print 했을 때 나오는 거???
    # print(new_row) 하면 저장된 위치(메모리 정보)만 나온다.
    # 하지만, 아래를 지정하면, 저장된 위치가 아니라 다음 문구가 나오게 해준다.
    # 원래 존재하는 __str__의 역할을 바꿔준 것.
    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        # self.pk는 변수중에 없는데???
        # id를 뜻한다. 이게 pk임. self.id 써도 무관.
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성됨


# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#field-types
# 사용할 수 있는 필드들의 종류 + 옵션. 보고 잘 결정하기.

# GuessNumbers.num_lotto 이렇게 변수를 바로 호출할 수 있다. 안정했으면 default 값인 5가 나오겠지.
# new_row = GuessNumbers(name=user_input_name, text=user_input_text)
# 하나의 행에 들어있는 열의 값 꺼내서 수정도 가능. new_row.name = new_row.name.upper(0)
# new_row.lottos = [np.randint(1, 50) for i in range(6)
