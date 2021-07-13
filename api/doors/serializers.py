from rest_framework import serializers

from .models        import DoorUseLog

class DoorUseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DoorUseLog
        exclude = ('id',)

    def validate_door_number(self, value):
        if not len(value) == 4:
            raise serializers.ValidationError()
        return value
    
    def validate_password(self, value):
        if not len(value) == 4:
            raise serializers.ValidationError()
        return value

class DoorSearchSerializer(serializers.Serializer):
    door_number = serializers.CharField(max_length=4)
    password    = serializers.CharField(max_length=4)