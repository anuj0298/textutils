#i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get("text",'default')
    removepunc= request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newliner=request.GET.get('newliner','off')
    spaceremover=request.GET.get('spaceremover','off')
    charcounter=request.GET.get('charcounter','off')

    if removepunc== 'on':
        analyzed= ""
        punctuation=''' .,;':""/?><!' '''
        for char in djtext:
            if char not in punctuation:
                analyzed+= char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        djtext= analyzed
    if fullcaps== 'on':
        analyzed=""
        for char in djtext:
            analyzed+= char.upper()
        params={'purpose':'capitalize text','analyzed_text':analyzed}
        djtext= analyzed
    if newliner == 'on':
        analyzed= ""
        for char in djtext:
            if char != "\n":
                analyzed+= char
        params={'purpose':'removed new lines','analyzed_text':analyzed}
        djtext=analyzed
    if spaceremover == 'on':
        analyzed= ""
        for char in djtext:
            if char != "   ":
                analyzed+= char
        params={'purpose':'removed space','analyzed_text':analyzed}
        djtext=analyzed
    if charcounter == 'on':
        analyzed= 0
        for char in djtext:
            if char != "  ":
                analyzed+= 1
        params={'purpose':'no. of characters is','analyzed_text':analyzed}
    if (charcounter!= 'on' and spaceremover!= 'on' and fullcaps!= 'on' and removepunc!='on' and newliner!= 'on'):
        return HttpResponse("please select minimum one operation and try agein...")
    return render(request,'analyze.html',params)
