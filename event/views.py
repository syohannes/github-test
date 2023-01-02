from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Post 

class EventListView(ListView):
    model = Post
    template_name = 'event/home.html'
class EventDetailView(DetailView):
    model = Post
    template_name = 'event/post_detail.html'
class EventCreateView(CreateView):
    model = Post
    template_name = 'event/event_new.html'
    fields = '__all__'
class EventUpdateView(UpdateView):
    model = Post
    template_name = 'event/event_edit.html'
    fields = ['title', 'body', 'qoutes']
class EventDeleteView(DeleteView):
    model = Post
    template_name = 'event/event_delete.html'
    success_url = reverse_lazy('home')
    