from .models import *
from rest_framework import serializers

class SingerSerializer(serializers.ModelSerializer):
    """
    StringRelatedField:
        It shows the title or name of an object.
    """
    song = serializers.StringRelatedField(many=True, read_only=True)    

    """
    PrimaryRelatedKey:
        PrimaryKeyRelatedField shows the primary key, default primary key is `id`.
    """
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """
    HyperlinkedRelatedField:
        This will create links of that related foriegn keys (songs), `-detail` is compulsary to pass at the end of each name
        in the parameter (view_name) 

    """
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')    
    """
    SlugRelatedField:
        slug related field ma hm slug_field jo k aik parameter ha, is ma koi b field pass kry gy tu wo automatically
        api ma show hoga, age title kry gy tu title ya phr duration kr gy tu duration
    """
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    """
    HyperlinkedIdentityField:
        This is similiar to HyperlinkedRelatedFeild, the main difference is it shows only one foriegn key, and  
        HyperlinkedRelatedFeild show many foriegn keys.
    """
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')


    class Meta:
        model = Singer
        fields = [
            'first_name',
            'gender',
            'song', # this is the related_name mentioned in the foriegn key of other model
        ]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
