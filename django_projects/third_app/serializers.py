from rest_framework import serializers
from .models import customer_data, practice, apis

class customer_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer_data
        fields = '__all__'

class practiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = practice
        fields = '__all__'

class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model = apis
        fields = "__all__"