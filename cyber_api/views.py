from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import PersonSerializers, QuestionSerializer, OptionSerializer,TopicSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .models import Person, Question, Quiz, Topic
import random


@api_view(['POST'])
def PersonAdd(request):
    if request.method == 'POST':
        serializer = PersonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Bu yerda create() metodi chaqiriladi
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def GetPerson(request, pk):
    if request.method == "GET":
        try:
            user = Person.objects.get(telegram_id=pk)
            serializer = PersonSerializers(user)
            return Response(serializer.data, status=200)
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status=404)
        

class TopicApi(APIView):
    def get(self, request, title):
        data = Topic.objects.get(title=title)
        serializer = TopicSerializer(data)
        return Response(serializer.data)

class TestTemplate(APIView):
    def get(self, request):
        try:
            data = Question.objects.order_by('?')
            serializer = QuestionSerializer(data, many=True)
            return Response(serializer.data[:20])
        except Question.DoesNotExist:
            return JsonResponse({"ok":"test topilmadi."})
    
        