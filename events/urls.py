from django.urls import path
from .views import (
    EventListCreateView,
    EventDetailView,
    RSVPCreateView,
    EventRSVPListView
)

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:event_id>/rsvps/', EventRSVPListView.as_view(), name='event-rsvps'),
    path('rsvp/', RSVPCreateView.as_view(), name='rsvp-create'),
]
