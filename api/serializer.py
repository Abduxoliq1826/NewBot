from rest_framework import serializers
from main.models import *

class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = "__all__"

class BotinfoSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = BotDetail
        fields = "__all__"
