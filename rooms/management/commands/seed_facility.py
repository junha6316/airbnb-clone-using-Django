from django.core.management.base import BaseCommand
from rooms import models as room_model
from sys import stdout


class Command(BaseCommand):
    def handle(self, *args, **options):
        facilities = ["건물 내 무료 주차", "헬스장", "자쿠지", "수영장"]
        for facility in facilities:
            room_model.Facility.objects.create(name=facility)

        self.stdout.write(self.style.SUCCESS("Facilities Created"))