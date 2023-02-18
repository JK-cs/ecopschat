from django.db import models

class Room(models.Model):
    # 유일성 체크 하지 않으므로 동일한 이름의 방도 가능
    name=models.CharField(max_length=100)

    @property
    def chat_group_name(self):
        return self.make_chat_group_name(room=self)

    @staticmethod
    def make_chat_group_name(room=None, room_pk=None):
        return "chat-%s" % (room_pk or room.pk)

