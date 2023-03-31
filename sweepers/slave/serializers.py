from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.exceptions import ValidationError


class SweeperSerializer(serializers.ModelSerializer):


    class Meta:
        model = Sweeper
        fields = '__all__'
    validators = [
        UniqueTogetherValidator(
        queryset = Sweeper.objects.all(),
        fields= ['first_name', 'last_name'],
        message='First name and Last name already exists.'
        )
    ]

    def validate_cleaning_frequency(self, value):
        if value > 1000:
            raise serializers.ValidationError(
                'Must be lesser then "1000".'
            )
        return value
    
    # def validate_first_name(self, value):
    #     if Sweeper.first_name == 'fuck' or Sweeper.first_name == 'Fuck':
    #         raise serializers.ValidationError(
    #             'This name is fucking incorrect.'
    #         )
    #     return value
