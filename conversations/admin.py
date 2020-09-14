from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Message)
class MessageAdimin(admin.ModelAdmin):
    list_display = ("__str__", "created")
    pass


@admin.register(models.Conversation)
class ConversationsAdmin(admin.ModelAdmin):
    list_display = ("__str__","count_message",)
