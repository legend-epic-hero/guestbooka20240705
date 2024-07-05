from django.urls import path
from .import views

urlpatterns = [
    # massage/     =>  留言列表
    path('', views.MassageList.as_view(), name='msg_list'),
    #massage/1/, massage/2/, ...
    path('<int:pk>/', views.MassageRead.as_view(), name='msg_read'),

    path('create/', views.MassageNew.as_view(), name='msg_create'),

    path('<int:pk>/delete/', views.MassageDelete.as_view(), name='msg_delete')

]
