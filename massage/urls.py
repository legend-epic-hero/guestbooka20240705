from django.urls import path
from .import views

urlpatterns = [
    # massage/     =>  留言列表
    path('', views.MassageList.as_view(), name='msg_list'),
    #massage/1/, massage/2/, ...
    path('<int:pk>/', views.MassageRead.as_view(), name='msg_read'),

    path('', views.MassageNew.as_view(), name='msg_new')

   
]
