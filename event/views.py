from django.views.generic import ListView, DetailView
from . models import Post 

class EventListView(ListView):
    model = Post
    template_name = 'event/home.html'
class EventDetailView(DetailView):
    model = Post
    template_name = 'event/post_detail.html'