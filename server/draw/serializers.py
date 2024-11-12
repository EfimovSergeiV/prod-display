from rest_framework import serializers
from draw.models import DrawingModel



class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrawingModel
        fields = '__all__'
