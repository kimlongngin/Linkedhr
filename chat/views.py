from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def home(request):
    title = "my chat room"
    return render(request, 'index.html', {"title":title})

def chat(request):
    if request.method !="POST":
        return HttpResponseRedirect(reverse('index'))
    else:
        title = "Chat room"
        username = request.POST.get('username')
        print("User Name "+ username)
        return render(request, 'chat.html', {"title":title, "username":username})