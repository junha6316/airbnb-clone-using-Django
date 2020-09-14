from django.contrib import admin
from . import models
import datetime

# Register your models here.
@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Reservation Admin Definiton """

    list_display = ("room", "check_in", "check_out", "InProgressed", "is_finished")
    list_filter = ("status",)
