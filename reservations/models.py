from django.db import models
from core import models as core_models
from django.utils import timezone

# 파이썬 타임 라이브러리를 사용하지 않는 이유
# 서버 시간을 기준으로 관리하고 싶기 때문에


class Reservation(core_models.TimeStampedModel):
    STATUS_PENDING = "pending"
    STATUS_CONFIRM = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_CANCELED, "Canceled"),
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRM, "Confirm"),
    )
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()

    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def InProgressed(self):
        now = timezone.now().date()
        return self.check_in < now < self.check_out

    InProgressed.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return self.check_out < now

    is_finished.boolean = True


# Create your models here.
