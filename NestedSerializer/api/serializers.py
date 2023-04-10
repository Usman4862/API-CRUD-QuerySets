from .models import *
from rest_framework import serializers



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    # we are getting all the details of the SongSerializer and it is nested, and SerializerRelation is a Different topic
    song = SongSerializer(many=True, read_only=True)    

    class Meta:
        model = Singer
        fields = [
            'first_name',
            'gender',
            'song', # this is the related_name mentioned in the foriegn key of other model
        ]