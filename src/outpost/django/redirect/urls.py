from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^create/$", views.CreateView.as_view(), name="create"),
    url(r"^edit/(?P<pk>\d+)/$", views.UpdateView.as_view(), name="edit"),
    url(r"^delete/(?P<pk>\d+)/$", views.DeleteView.as_view(), name="delete"),
    url(r"^(?P<slug>[\w\d]+)$", views.RedirectView.as_view(), name="redirect"),
    url("$", views.IndexView.as_view(), name="index"),
]
