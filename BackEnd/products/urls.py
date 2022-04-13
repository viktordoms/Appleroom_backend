from django.urls import include, path

from .views import CategoriesListView

urlpatterns = [
    path('categories/', CategoriesListView.as_view())
]
