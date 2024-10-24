from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(["POST"])
def PersonAdd(request):
    if request.method == 'POST':
        name = request.data

        print(name)
        return JsonResponse({"name":name})
    return HttpResponse("ok")