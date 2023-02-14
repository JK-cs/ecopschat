from django.urls import path
from ouncechat import views

app_name = "ouncechat"

urlpatterns=[
    path("",views.index, name="index"),
]