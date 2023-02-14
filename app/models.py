from django.db.models.signals import post_save, post_delete
import django.db.models.signals
import django.urls
from django.db import models
from app.mixins import ChannelLayerGroupSendMixin


class Post(ChannelLayerGroupSendMixin, models.Model):
    CHANNEL_LAYER_GROUP_NAME = "liveblog"
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ["-id"]

def post__on_post_save(instance: Post, created: bool, **kwargs):
    if created:
        message_type = "liveblog.post.created"
    else:
        message_type = "liveblog.post.updated"

    post_id = instance.pk
    post_partial_url= django.urls.reverse("post_partial", args=[instance.pk])

    instance.channel_layer_group_send({
        "type": message_type,
        "post_id": post_id,
        "post_partial_url": post_partial_url,
    })

post_save.connect(
    post__on_post_save,
    sender=Post,
    dispatch_uid="post__on_post_save",
)

