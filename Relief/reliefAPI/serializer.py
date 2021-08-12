from .models import videoLink
from rest_framework import serializer

class videoSerializer(serializer.ModelSerializer):
    class Meta:
        model = videoLink
        fields = ["name","urlVideo","bookmark"]