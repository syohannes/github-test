from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
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