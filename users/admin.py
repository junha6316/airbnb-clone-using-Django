from django.contrib.admin.utils import flatten
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)  # admin 화면에서 사용할 Custom admin Panel에서 사용할 model을 갖고 있음
# decorator #admin.site.registe(models.User, CustomUserAdmmin)
class CustomUserAdmin(UserAdmin):
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("gender", "language", "currency")
    fieldsets = UserAdmin.fieldsets + (
        ("Banana", {"fields": ("avatar", "gender", "bio")}),
    )


# 장고 ad∫min이 할 수 있는 것
# list display
