from django.http.response import HttpResponse
from django.shortcuts import render
import logging
from django.urls import reverse_lazy
from django.views import generic
from .forms import InquiryForm
from django.contrib import messages


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name="diary/index.html"

class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary
class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries


class DiaryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Diary
    template_name ='diary_detail.html'

# 270

from .forms import InquiryForm, DiaryCreateForm

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request,'日記を作成しました。')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request,'日記の作成に失敗しました。')
        return super().form_invalid(form)

class DiaryUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('diary:diary_detail',kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request,'日記を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.reqest,"日記の更新に失敗しました。")
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request,*args,**kwargs):
        messages.success(self.request,"日記を削除しました。")
        return super().delete(request,*args,**kwargs)

