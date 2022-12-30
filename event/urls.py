from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='post_detail'),
    path('event/new/', EventCreateView.as_view(), name='event_new' ),
]