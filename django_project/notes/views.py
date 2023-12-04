from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from notes.models import Note, Topic


class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body', 'topic']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'body']

    def test_func(self):
        return self.request.user == self.get_object().created_by


class NoteDelete(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:note-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user == self.object.created_by

class TopicListView(ListView):
    model = Topic


class TopicDetailView(DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(topic=self.get_object().pk)
        return context


class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'parent', 'is_public']
    success_url = reverse_lazy('notes:topic-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TopicCreate, self).form_valid(form)


class TopicUpdate(UserPassesTestMixin, UpdateView):
    model = Topic
    fields = ['title', 'parent', 'is_public']

    def test_func(self):
        return self.request.user == self.get_object().created_by


class TopicDelete(UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy('notes:topic-list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user == self.object.created_by