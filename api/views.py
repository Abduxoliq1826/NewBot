import http

from rest_framework.response import Response
from .serializer import *
from main.models import *
from rest_framework.decorators import api_view

@api_view(['GET'])
def ViewsScience(request):
    room = Science.objects.all()
    return Response(ScienceSerializer(room, many=True).data)




@api_view(['POST'])
def AddStudent(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    phone_number1 = request.POST['phone_number1']
    phone_number2 = request.POST['phone_number2']
    age = request.POST['age']
    free_time = request.POST['free_time']
    science = request.POST['science']
    science1 = Science.objects.get(name=science)
    query = Student.objects.create(first_name=first_name,
                                   last_name=last_name,
                                   phone_number1=phone_number1,
                                   phone_number2=phone_number2,
                                   age=age,
                                   free_time=free_time,
                                   science=science1)

    return Response(data={"status":StudentSerializer(query)})

@api_view(['GET'])
def BotInfo(request):
    info = Bot.objects.last()
    return Response(BotSerializer(info).data)

@api_view(['GET'])
def BotDetaill(request):
    detail = BotDetail.objects.last()
    return Response(BotinfoSerizlizer(detail).data)