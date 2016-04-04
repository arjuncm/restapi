from user.models import User
from rest_framework import serializers

class FishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'active', 'created')
