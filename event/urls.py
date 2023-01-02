from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='post_detail'),
    path('event/new/', EventCreateView.as_view(), name='event_new' ),
    path('post/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('post/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
]    
