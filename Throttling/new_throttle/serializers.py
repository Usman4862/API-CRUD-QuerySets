from rest_framework import serializers
from .models import FakeThrottle
from rest_framework.validators import UniqueValidator

class FakeThrottleSerializer(serializers.ModelSerializer):

    class Meta:
        model = FakeThrottle
        fields = '__all__'



    # validators=[
    #     UniqueValidator(
    #     queryset= FakeThrottle.objects.all(),
    #     fields = ['name'],
    #     message = 'Name already exits',
    #     )
    # ]
    

    # def validate_age(self, value):
    #     if not (18 < value < 50):
    #         raise serializers.ValidationError("Age Must between 18-50")
    #     return value


