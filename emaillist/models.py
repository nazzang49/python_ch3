from django.db import models

# Create your models here.

# 테이블 생성
class Emaillist(models.Model):
    # DB에서 설정하는 varchar50과 같은 개념
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'Emaillist({self.first_name},{self.last_name},{self.email})'