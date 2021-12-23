from rest_framework import serializers
from .models import ContactPost

class ContactPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPost
        fields = '__all__'
        lookup_field = 'slug'