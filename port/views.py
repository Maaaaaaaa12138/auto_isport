from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
import port.isport
from .models import *

def index(request):
    statuss = Status.objects.filter(time=timezone.now())
    return render(request, "index.html", {"statuss": statuss})

def changeSession(request):
    session = request.GET.get("session")
    if session:
        se = JSESSIONID.objects.get(name="isport")
        se.content = session
        se.save()
        return HttpResponse("修改成功")
    
    return HttpResponse("修改失败")