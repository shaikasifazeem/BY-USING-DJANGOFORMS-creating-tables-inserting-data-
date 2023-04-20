from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
def insert_topic(request):
    TFO=TopicForms()
    d={'TFO':TFO}
    if request.method=='POST':
            TFD=TopicForms(request.POST)
            if TFD.is_valid():
                tname=TFD.cleaned_data['tname']   
            TO=Topic.objects.get_or_create(tname=tname)[0]
            TO.save()
            
            TQS=Topic.objects.all()
            d1={'TQS':TQS}
            return render(request,'displaytopic.html',d1)
    return render(request,'insert_topic.html',d)
# Create your views here.
def insert_web(request):
     
     WFO=WebpageForms()
     d={'WFO':WFO}
     if request.method=='POST':
          WFD=WebpageForms(request.POST)
          if WFD.is_valid():
               tname=WFD.cleaned_data['tname']
               TO=Topic.objects.get_or_create(tname=tname)[0]
               TO.save()
              
               name=WFD.cleaned_data['name']
               url=WFD.cleaned_data['url']
          WO=Webpage.objects.get_or_create(tname=TO,name=name,url=url)[0]
          WO.save()
          WQS=Webpage.objects.all()
          d1={'WQS':WQS}
          return render(request,'displayweb.html',d1)
     return render(request,'insert_web.html',d)

def insert_acces(request):
     AFO=AccessRecordForms()
     d={'AFO':AFO}
     if request.method=='POST':
          AFD=AccessRecordForms(request.POST)
          if AFD.is_valid():
               name=AFD.cleaned_data['name']
               WO=Webpage.objects.get_or_create(name=name)[0]
               WO.save()
               author=AFD.cleaned_data['author']
               date=AFD.cleaned_data['date']
          AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
          AO.save()
          AQS=AccessRecord.objects.all()
          d1={'AQS':AQS}
          return render(request,'displayacces.html',d1)
     return render(request,'insert_acces.html',d)