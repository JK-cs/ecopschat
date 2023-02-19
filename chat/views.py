from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from chat.forms import RoomForm
from chat.models import Room

# Create your views here.
#index뷰 수정
#Room 목록 조회 후 chat/index.html템플릿을 통해 Room목록 렌더링
def index(request):
    #Room쿼리셋을 생성, context data로 room_list 이름으로 넘김
    room_qs = Room.objects.all()
    return render(request, "chat/index.html",{
        "room_list":room_qs,
    })



def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            created_room: Room = form.save()
            return redirect("chat:room_chat", created_room.pk)
    else:
        form = RoomForm()

    return render(request, "chat/room_form.html",{
        "form":form,
    })
def room_chat(request, room_pk):
    room=get_object_or_404(Room,pk=room_pk)
    return render(request,"chat/room_chat.html",{
        "room":room,
    })

