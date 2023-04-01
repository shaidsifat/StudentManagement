from rest_framework import serializers
from .models import Classes


#classserilaizer for classes  model
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
