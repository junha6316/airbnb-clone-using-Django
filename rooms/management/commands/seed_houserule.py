from django.core.management.base import BaseCommand
from sys import stdout
from rooms import models as room_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        houseRules = ["반려동물 입실 가능", "흡연 가능"]
        for houseRule in houseRules:
            room_model.HouseRule.objects.create(name=houseRule)

        self.stdout.write(self.style.SUCCESS("HouseRule created"))