import os

from appconf import AppConf
from django.conf import settings


class RedirectAppConf(AppConf):
    HASH_LENGTH = 16

    class Meta:
        prefix = "redirect"
