from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import Physio_Form, Treatment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class Physio_FormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Physio_Form
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'