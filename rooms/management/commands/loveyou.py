from django.core.management.base import BaseCommand
from sys import stdout

class Command(BaseCommand):
    help = "this is Help"
    print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            help="How many times do you want me to tell you that I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("number")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS"i love you")
