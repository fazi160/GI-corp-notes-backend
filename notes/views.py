from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Notes
from .serializers import NotesSerializer


# this will allow all the functionalities based for the model notes. currently it has all the crud operations so because of that i used ModelViewset instead of generic or APIView. 
# by  default ModelViewSet will provide all the options (GET, POST, PATCH, DELETE).
class NotesView(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

