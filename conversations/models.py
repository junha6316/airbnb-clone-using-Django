from django.db import models
from core import models as core_models

# Create your models here.
class Conversation(core_models.TimeStampedModel):
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        participant = [username for username in self.participants.all()]
        # object.all() 객체를 대표하는 __str__을 이용해 값을 갖고 온다
        return ", ".join(map(str, participant))

    def count_message(self):
        return self.messages.count()

    count_message.short_description = "A number of Message"


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
