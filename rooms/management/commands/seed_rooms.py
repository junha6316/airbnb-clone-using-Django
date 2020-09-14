import random
from sys import stdout


from django_seed import Seed
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten

from rooms import models as room_model
from users import models as user_model


class Command(BaseCommand):
    help = "Make fake users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many creates Rooms", default=1, type=int
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = user_model.User.objects.all()  # 이렇게 사용하면 안된다.
        room_types = room_model.RoomType.objects.all()

        seeder = Seed.seeder()

        seeder.add_entity(
            room_model.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "baths": lambda x: random.randint(1, 10),
                "guests": lambda x: random.randint(1, 100),
                "bedrooms": lambda x: random.randint(1, 100),
                "price": lambda x: random.randint(100000, 100000000),
            },
        )

        created_photos = seeder.execute()
        # shape을 정리한다.
        created_clean = flatten(list(created_photos.values()))

        for pk in created_clean:
            room = room_model.Room.objects.get(pk=pk)
            for i in range(3, random.randint(5, 17)):
                room_model.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"/{random.randint(1,31)}.webp",
                    room=room,
                )

        self.stdout.write(self.style.SUCCESS("Rooms are created"))
