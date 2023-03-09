from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def login(request):
    return render(request, 'login.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = ""
    if len(room) != 11:
        room_details = Room.objects.get(name = room)
    return render(request, 'index.html', {'username': username, 'room_details':room_details, 'room':room})

def checkView(request):
    if request.method == 'POST':
        username = request.POST['username']
        room_name = request.POST['room']
        if Room.objects.filter(name = room_name).exists():
            return redirect("/"+room_name + "/?username=" + username)
        else:
            print("create new room")
            new_room = Room.objects.create(name = room_name)
            new_room.save()
            return redirect("/"+room_name + "/?username=" + username)
            
@csrf_exempt
def send(request):
    if request.method == 'POST':
        name = request.POST['username']
        text = request.POST['message']
        id_room = request.POST['room_id']
        if len(text) > 0:
            new_message = Message.objects.create(username = name, message = text, room_id = id_room)
            new_message.save()

        return JsonResponse({'success': True})   
    

def getMessages(request, room):
    room_detail=''
    if len(room) != 11:
        room_detail = Room.objects.get(name = room)


    message = Message.objects.filter(room_id = room_detail.id)
    return JsonResponse({'messages' : list(message.values())})