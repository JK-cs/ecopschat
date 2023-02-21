import django.contrib.messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from chat.forms import RoomForm
from chat.models import Room
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

# Create your views here.
#index뷰 수정
#Room 목록 조회 후 chat/index.html템플릿을 통해 Room목록 렌더링
def index(request):
    #Room쿼리셋을 생성, context data로 room_list 이름으로 넘김
    room_qs = Room.objects.all()
    return render(request, "chat/index.html",{
        "room_list":room_qs,
    })


@login_required
def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            created_room: Room = form.save(commit=False)
            created_room.owner=request.user
            created_room.save()
            return redirect("chat:room_chat", created_room.pk)
    else:
        form = RoomForm()

    return render(request, "chat/room_form.html",{
        "form":form,
    })

@login_required
def room_chat(request:HttpRequest, room_pk: int)->HttpResponse:
    room=get_object_or_404(Room,pk=room_pk)
    return render(request,"chat/room_chat.html",{
        "room":room,
    })

@login_required
def room_delete(request:HttpRequest, room_pk: int)->HttpResponse:
    room = get_object_or_404(Room, pk=room_pk)

    if room.owner != request.user:
        messages.error(request, "채팅방 소유자가 아닙니다.")
        return redirect("chat:index")

    if request.method =="POST":
        room.delete()
        messages.success(request, "채팅방을 삭제했습니다.")
        return redirect("chat:index")

    return render(request, "chat/room_confirm_delete.html",{
        "room": room,
    })






# class RoomCreateView(LoginRequiredMixin, CreateView):
#     form_class = RoomForm
#     template_name = "chat/room_form.html"
#
#     def get_success_url(self):
#         created_room=self.object
#         return resolve_url("chat:room_chat", created_room.pk)
#
# room_new




