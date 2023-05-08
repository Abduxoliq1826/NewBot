from django.shortcuts import render, redirect
from .models import *
from datetime import date
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def dashboard(request):
    context = {
        'student': Student.objects.all(),
        'student_': Student.objects.all().count(),
        'deleted_': Student.objects.filter(type=3).count(),
        'finished_': Student.objects.filter(type=2).count(),
        'news_': Student.objects.filter(type=1).count(),

    }
    return render(request, 'index.html', context)

def Finished(request):
    context = {
        'finished': Student.objects.filter(type=2),
        'student_': Student.objects.all().count(),
        'deleted_': Student.objects.filter(type=3).count(),
        'finished_': Student.objects.filter(type=2).count(),
        'news_': Student.objects.filter(type=1).count(),
    }
    return render(request, "finished.html",context)

def Deleted(request):
    context = {
        'deleted': Student.objects.filter(type=3),
        'student_': Student.objects.all().count(),
        'deleted_': Student.objects.filter(type=3).count(),
        'finished_': Student.objects.filter(type=2).count(),
        'news_': Student.objects.filter(type=1).count(),
    }
    return render(request, "deleted.html",context)

def News(request):
    context = {
        'news': Student.objects.filter(type=1),
        'student_': Student.objects.all().count(),
        'deleted_': Student.objects.filter(type=3).count(),
        'finished_': Student.objects.filter(type=2).count(),
        'news_': Student.objects.filter(type=1).count(),
    }
    return render(request, "news.html",context)


def News_deleted(request, pk):
    newss = Student.objects.get(id=pk)
    newss.type = 3
    newss.save()
    return redirect("news")

def News_finished(request, pk):
    newss = Student.objects.get(id=pk)
    newss.type = 2
    newss.save()
    return redirect("news")


def Deleted_finished(request, pk):
    deleted = Student.objects.get(id=pk)
    deleted.type = 2
    deleted.save()
    return redirect("deleted")


def Finished_deleted(request, pk):
    finished = Student.objects.get(id=pk)
    finished.type = 3
    finished.save()
    return redirect("news")

def Add_Bot(request):
    text = request.POST.get('text')
    name = request.POST.get('name')
    Bot.objects.create(text=text, name=name)
    return redirect("bot")

def Add_BotDeteil(request):
    text = request.POST.get('text')
    lat = request.POST.get('lat')
    lng = request.POST.get('lng')
    BotDetail.objects.create(text=text, lat=lat, lng=lng)
    return redirect("bot_detail")

def AddScience(request):
    name = request.POST.get('name')
    Science.objects.create(name=name)
    return redirect("science")

def Bot_views(request):
    context = {
        'bot': Bot.objects.all(),
    }
    return render(request, 'bot.html', context)

def Science_view(request):
    context = {
        'science': Science.objects.all(),
    }
    return render(request, 'science.html', context)


def BotDetail_views(request):
    context = {
        "bot_detail": BotDetail.objects.all()
    }
    return render(request, 'bot_detail.html',context)

def Delete_Bot(request, pk):
    bot = Bot.objects.get(id=pk)
    bot.delete()
    return redirect('bot')

def DeleteScience(request, pk):
    bot = Science.objects.get(id=pk)
    bot.delete()
    return redirect('science')

def Delete_BotDetail(request, pk):
    botdetail = BotDetail.objects.get(id=pk)
    botdetail.delete()
    return redirect('bot_detail')


