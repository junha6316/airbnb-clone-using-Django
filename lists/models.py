from django.db import models
from core import models as core_model

# Create your models here.


class List(core_model.TimeStampedModel):
    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return len(self.room.all())
