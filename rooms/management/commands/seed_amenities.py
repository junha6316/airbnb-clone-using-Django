"""
Seed fake amenities data 
"""
from django.core.management.base import BaseCommand
from rooms import models as room_models
from sys import stdout


class Command(BaseCommand):
    def handle(self, *args, **options):
        amenities = [
            "주방",
            "샴푸",
            "난방",
            "에어컨",
            "세탁기",
            "건조기",
            "무선 인터넷",
            "아침식사",
            "실내 벽난로",
            "옷걸이",
            "다리미",
            "헤어드라이어",
            "노트북 작업 공간",
            "TV",
            "유아용 식탁의자",
            "셀프 체크인",
            "화재경보기",
            "일산화탄소 경보기",
            "욕실 단독 사용",
            "수변에 인접",
            "스키를 탄 채로 출입 가능",
        ]
        for amenity in amenities:
            room_models.Amenity.objects.create(name=amenity)
        self.stdout.write(self.style.SUCCESS("Amenities Created"))
