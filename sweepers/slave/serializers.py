from rest_framework import serializers
from .models import *

class SweeperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sweeper
        fields = '__all__'
