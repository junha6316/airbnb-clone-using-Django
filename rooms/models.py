# Python

# Django
from django.db import models
from django.urls import reverse

# 3rd Party Apps
from django_countries.fields import CountryField

# My apps
from core import models as core_models
from users import models as users_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name_plural = "Room Types"


class Amenity(AbstractItem):
    """Amenity Model Definintion"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Faciliites"


class HouseRule(AbstractItem):

    """HouseRule Mdoel Definition"""

    class Meta:
        verbose_name_plural = "House Rules"


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)  # 필수정보
    description = models.TextField()
    country = CountryField()
    # Django Country를 이용해 모든 나라의 이름을 넣어줄거다
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()

    bedrooms = models.IntegerField()
    baths = models.IntegerField()

    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(
        users_models.User, related_name="rooms", on_delete=models.CASCADE
    )

    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True, blank=True
    )  # Room Type 이 제거되도 없어지지 않게 한다.

    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    houseRules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def save(self, *args, **kwargs):  # Room 모델에서 save 함수를 다시 정의한다.

        """Override Save Method"""

        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)
        return 0

    def get_absolute_url(self, **kwargs):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    def Rating_Reviews(self):
        all_review = self.reviews.all()
        all_rating = [review.rating_average() for review in all_review]

        return (
            round(sum(all_rating) / len(all_rating), 2)
            if len(all_rating) != 0
            else "None"
        )

    Rating_Reviews.short_description = "Avg"
    
    def first_photo(self):
        photo, = self.photos.all()[:1]
        return photo.file.url





class Photo(core_models.TimeStampedModel):

    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        "Room", related_name="photos", on_delete=models.CASCADE
    )  # String으로 선언하면 import 하지 않아도 된다.

    def __str__(self):
        return self.caption


    
