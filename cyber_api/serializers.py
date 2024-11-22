from rest_framework import serializers
from .models import (Person, Question, Option, Topic)

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct'] 

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)  

    class Meta:
        model = Question
        fields = ['id', 'title', 'img', 'option_type', 'date_created', 'date_update', 'options']

