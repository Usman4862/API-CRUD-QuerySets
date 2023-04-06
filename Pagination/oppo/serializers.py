from rest_framework import serializers
from .models import *


class OppoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OppoModel
        fields = '__all__'

    