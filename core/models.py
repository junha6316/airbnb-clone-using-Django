from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # 모델이지만 데이터베이스에 들어가지 않는다.
        # 추상 클래스