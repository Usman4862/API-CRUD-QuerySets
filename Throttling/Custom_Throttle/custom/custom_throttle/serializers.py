from rest_framework import serializers
from .models import FakeThrottle
from rest_framework.validators import UniqueValidator

class FakeThrottleSerializer(serializers.ModelSerializer):

    class Meta:
        model = FakeThrottle
        fields = '__all__'

