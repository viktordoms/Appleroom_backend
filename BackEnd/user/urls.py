from django.urls import include, path

from .views import UserProfileListView, UserProfileDetailView, UserCreate

urlpatterns = [
    path("register/", UserCreate.as_view(), name="register"),
    path("all-profiles/", UserProfileListView.as_view(), name="all-profiles"),
    path("profile/<int:pk>/", UserProfileDetailView.as_view(), name="profile"),
]
