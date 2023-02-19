from django.db import models

class Room(models.Model):
    name=models.CharField(max_length=100)

    @property
    def chat_group_name(self):
        return self.make_chat_group_name(room=self)

    @staticmethod
    def make_chat_group_name(room=None, room_pk=None):
        return "chat-%s" % (room_pk or room.pk)

    #Room모델 수정: 셋에 default정렬 지정
    #대개 하나의 기준으로 정렬하는데 default로 지정 시 매번 정렬 필요 X
    class Meta:
        ordering=["-pk"]

