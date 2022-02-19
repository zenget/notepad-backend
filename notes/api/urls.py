from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notes.api import views as cv

router = DefaultRouter()
router.register(r"notes", cv.NoteSerializerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
