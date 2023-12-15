from rest_framework import serializers

from .models import Notes

# Serializer for converting Notes model instances to JSON and vice versa
class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'