from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotesView

router = DefaultRouter()
router.register(r'notes', NotesView, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]