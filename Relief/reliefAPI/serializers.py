from .models import videoLink
from rest_framework import serializers

#Serialize the data

class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoLink
        fields = ["name","urlVideo","bookmark"]
        