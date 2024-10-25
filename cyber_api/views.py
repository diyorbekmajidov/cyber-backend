from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializers import PersonSerializers
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def PersonAdd(request):
    if request.method == 'POST':
        serializer = PersonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Bu yerda create() metodi chaqiriladi
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        