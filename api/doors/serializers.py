from rest_framework import serializers

from .models import DoorUseLog

class DoorUseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorUseLog
        exclude = ('id',)

    

