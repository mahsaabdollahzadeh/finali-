from  rest_framework import serializers
from .models import fly
class flyserializer(serializers.ModelSerializer):
    class meta :
        model = fly
        fields = '__all__'

