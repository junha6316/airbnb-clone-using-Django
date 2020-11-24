import random
from sys import stdout

from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed

import rooms.models as room_models
import users.models as user_models
import lists.models as list_models


NAME = "lists"


class Command(BaseCommand):

    help = f"Make fake {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help=f"How many creates {NAME}", default=1, type=int
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder = Seed.seeder()

        seeder.add_entity(
            list_models.List,
            number,
            {"user": random.choice(users)},
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.room.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} are created"))
