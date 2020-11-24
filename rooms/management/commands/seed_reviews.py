import random

from django_seed import Seed
from django.core.management.base import BaseCommand


import reviews.models as review_models
import users.models as user_models
import rooms.models as room_models


class Command(BaseCommand):
    help = "Make fake users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many creates Rooms", default=1, type=int
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder = Seed.seeder()

        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "check_in": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "room": lambda x: random.choice(rooms),
                "user": lambda x: random.choice(users),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews are created"))
