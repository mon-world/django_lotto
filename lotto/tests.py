from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
# 서비스 내에 기능들이 정상적으로 작동하는지 테스트 한다.
class GuessNumbersTestCase(TestCase): # 반드시 이걸 상속받음
    
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')
        g.generate()

        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos) > 20) # True여야 통과.