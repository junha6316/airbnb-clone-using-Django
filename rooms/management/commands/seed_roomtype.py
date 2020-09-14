from django.core.management.base import BaseCommand
from sys import stdout
from rooms import models as room_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        roomtypes = ["주택", "아파트", "게스트용 별채", "레지던스", "로프트", "저택", "전원주택"]
        for roomtype in roomtypes:
            room_model.RoomType.objects.create(name=roomtype)
        self.stdout.write(self.style.SUCCESS("rommtypes created"))
