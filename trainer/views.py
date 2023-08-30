from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from feedback.models import Feedback
from student.models import Student
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


# Create your views here.

class TrainerCreateView(LoginRequiredMixin,CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    # fields = '__all__'
    form_class = TrainerForm
    success_url = reverse_lazy('home-page')


class TrainerListView(LoginRequiredMixin,ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'

    def get_queryset(self):
        return Trainer.objects.filter(active=True)


class TrainerUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'student/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list_of_trainers')


class TrainerDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list_of_trainers')


class TrainerDetailView(LoginRequiredMixin,DetailView):
    template_name = 'trainer/detail_trainer.html'
    model = Trainer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()  # preluam data si ora curenta
        context[
            'current_datetime'] = now  # adaugam in dictionarul context, cheia current_datetime pentru a afisa data si ora curenta

        current_trainer_id = self.kwargs['pk']  # accesam id-ul trainerului selectat
        students = Student.objects.filter(
            trainer_id=current_trainer_id)  # realizam un query prin luam toti studenti asignati trainerului selectat
        context[
            'students'] = students  # trimitem in interfata pe baza cheii studente, toti studentii asignati trainerului selectat
        feedbacks = Feedback.objects.filter(
            trainer_id=current_trainer_id)
        context['feedbacks'] = feedbacks


        return context

# get_context_data este o metoda folosit in clasele de View-uri (ListView, TemplateView, UpdateView, CreateView etc) care
# este utilizata pentru a construi si return un dictionat de date de context care vor fi afisate in paginile html

