from rest_framework import serializers
from .models import Sample


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='example-detail',
        lookup_field='id'
    )
    class Meta:
        model = Sample
        fields = [
            'id',
            'first_name',
            'city',
            'roll',
            'url',
        ]
        lookup_field = 'id'
