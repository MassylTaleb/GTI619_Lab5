from rest_framework import serializers
from .models import *

class ParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Params
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

