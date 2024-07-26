from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreViewSet,
    CinemaHallViewSet,
    ActorViewSet,
    MovieViewSet
)


router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"actor", ActorViewSet)
router.register(r"cinema_hall", CinemaHallViewSet)
router.register(r"genre", GenreViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "cinema"
