import random
import string

from django.db import models
from django.db.models.signals import post_init
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from guardian.models import (
    GroupObjectPermissionBase,
    UserObjectPermissionBase,
)

from .conf import settings


class RedirectUrl(models.Model):
    slug = models.CharField(null=False, max_length=settings.REDIRECT_HASH_LENGTH)
    destination = models.URLField(verbose_name=_("Ziel URL"), max_length=400)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.slug} --> {self.destination}"

    @classmethod
    def post_init(cls, sender, instance, **kwargs):
        if cls is not sender:
            return
        if instance.slug:
            return
        instance.slug = "".join(
            random.choices(
                string.ascii_letters + string.digits, k=settings.REDIRECT_HASH_LENGTH
            )
        )


post_init.connect(RedirectUrl.post_init)


class RedirectUrlForm(ModelForm):
    class Meta:
        model = RedirectUrl
        fields = ["destination"]
