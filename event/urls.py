from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('post/<int:pk>/', EventDetailView.as_view(), name='post_detail'),
    
]