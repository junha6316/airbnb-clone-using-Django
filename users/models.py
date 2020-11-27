import uuid

from django.db import models
from django.conf import settings
from django.utils.html import strip_tags
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.template.loader import render_to_string


class User(AbstractUser):
    # 장고가 form을 만들어준다.
    # 기본 AbstractUser의 __str__ => username

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Ohter"),
    )

    LANGUAGE_ENGLIGH = "en"
    LANGUAGE_KOREAN = "ko"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLIGH, "English"), (LANGUAGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    username = models.CharField(max_length=120, unique=True)
    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(upload_to="avartar", blank=True, null=True)
    gender = models.CharField("성별", max_length=10, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        "언어",
        max_length=2,
        choices=LANGUAGE_CHOICES,
        blank=True,
        default=LANGUAGE_KOREAN,
    )
    currency = models.CharField(
        "통화", max_length=2, choices=CURRENCY_CHOICES, default=CURRENCY_USD
    )
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify Airbnb Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
