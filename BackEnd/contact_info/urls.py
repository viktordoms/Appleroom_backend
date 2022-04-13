from django.urls import include, path

from .views import MainInfoView

urlpatterns = [
    path("info/", MainInfoView.as_view())
]
