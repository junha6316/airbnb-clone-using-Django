from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width = 50px src ={obj.file.url} />")

    get_thumbnail.short_description = "Thumbnail"


# class PhotoInline(admin.TabularInline):
class PhotoInline(admin.StackedInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition"""

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic_Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "bedrooms",
                    "baths",
                ),
            },
        ),
        (
            "More About the Space",
            {
                "fields": (
                    "amenities",
                    "facilities",
                    "houseRules",
                )
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "guests",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "countItems",
        "Count_Photos",
        "Rating_Reviews",
    )
    ordering = ("price",)

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "amenities",
        "facilities",
        "houseRules",
        "country",
        "city",
    )
    raw_id_fields = ("host",)  # Item들을 아이디를 이용해 관리하게 한다.

    search_fields = ("^city", "host__username")

    filter_horizontal = (  # filter_horizontal
        "amenities",
        "facilities",
        "houseRules",
    )

    def save_model(self, request, obj, form, change):
        print(obj, change, form)
        super().save_model(request, obj, form, change)

    def countItems(self, obj):  # self: admin class /obj : current row
        return obj.amenities.count()  # queryset

    def Count_Photos(self, obj):
        return obj.photos.count()

    Count_Photos.short_description = "Photo Count"


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(selfm, obj):  # ROOMS THAT HAVE THE ITEM
        return obj.rooms.count()


# Register your models here.
