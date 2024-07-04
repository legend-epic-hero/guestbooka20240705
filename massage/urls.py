from django.urls import path
from .import views

urlpatterns = [
    # massage/     =>  留言列表
    path('', views.MassageList.as_view(), name='msg_list'),
   
]
