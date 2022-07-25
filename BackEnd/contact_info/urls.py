from django.urls import include, path

from .views import CityInfoView

urlpatterns = [
    path("city/", CityInfoView.as_view())
]
