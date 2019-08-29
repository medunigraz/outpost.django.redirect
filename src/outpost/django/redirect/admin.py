from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import assign_perm

from .models import RedirectUrl


class RedirectUrlAdmin(GuardedModelAdmin):
    list_display = ("pk", "slug", "destination", "enabled")
    list_filter = ("enabled",)
    fields = ("destination", "enabled")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        assign_perm("delete_redirecturl", request.user, obj)
        assign_perm("change_redirecturl", request.user, obj)


admin.site.register(RedirectUrl, RedirectUrlAdmin)
