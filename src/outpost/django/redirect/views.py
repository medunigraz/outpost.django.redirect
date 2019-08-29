from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy as reverse
from django.views import generic
from guardian.mixins import (
    LoginRequiredMixin,
    PermissionListMixin,
    PermissionRequiredMixin,
)
from guardian.shortcuts import assign_perm

from .models import RedirectUrl, RedirectUrlForm


class RedirectView(generic.RedirectView):

    http_method_names = ["get", "head", "options"]

    def get_redirect_url(self, *args, **kwargs):
        redir = get_object_or_404(RedirectUrl, slug=kwargs.get("slug"), enabled=True)
        return redir.destination


class CreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):

    model = RedirectUrl
    fields = ("destination", "enabled")
    success_url = reverse("redirect:index")
    permission_required = "redirect.add_redirecturl"
    accept_global_perms = True
    permission_object = None

    def form_valid(self, form):
        result = super().form_valid(form)
        assign_perm("delete_redirecturl", self.request.user, self.object)
        assign_perm("change_redirecturl", self.request.user, self.object)
        return result


class UpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):

    model = RedirectUrl
    fields = ("destination", "enabled")
    success_url = reverse("redirect:index")
    permission_required = "redirect.change_redirecturl"


class DeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):

    model = RedirectUrl
    success_url = reverse("redirect:index")
    permission_required = "redirect.delete_redirecturl"


class IndexView(LoginRequiredMixin, PermissionListMixin, generic.ListView):

    model = RedirectUrl
    permission_required = ("delete_redirecturl", "change_redirecturl")
    get_objects_for_user_extra_kwargs = {"any_perm": True}
