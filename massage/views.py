from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Massage
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MassageList(ListView):
    model = Massage
    ordering = ['-id']

    # 頁面範本檔案名稱:應用程式/資料模型_list.html => massage/massage_list.html

class MassageRead(DetailView):
    model = Massage

    #頁面範本檔案名稱:應用程式/資料模型_detail.html => massege/massage_detail......
    #頁面範本變數名稱:資料模型=> massage

class MassageNew(CreateView):
    model = Massage
    fields = ['user', 'receipt', 'subject', 'content'] 
    success_url= reverse_lazy('msg_list') 

    #fields = '__all__'    ->顯示全部欄位

    #頁面範本檔案名稱:應用程式/資料模型_form.html => massege/massage_detail......
    #頁面範本變數名稱:資料模型=> massage

class MassageDelete(LoginRequiredMixin,DeleteView):
    model = Massage
    success_url = reverse_lazy('msg_list')
    # 頁面範本檔案名稱:應用程式/資料模型_confirm_delete.html => massage/Massage _confirm_delete.html