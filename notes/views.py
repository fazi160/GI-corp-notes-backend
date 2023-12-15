from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Notes
from .serializers import NotesSerializer



# Create your views here.

# this will allow all the functionalities based on the model notes
class NotesView(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

