from django.shortcuts import render
from django.http import HttpResponse
from core.models import Cause, Event, Trustee
# Create your views here.

def index(request):
    causes = Cause.objects.all()
    events = Event.objects.all()
    upcoming_events = [e for e in events if e.upcoming]
    trustees = Trustee.objects.all()
    return render(request, 'home/home.html', {'causes': causes, 'events': upcoming_events, 'trustees': trustees})


def contact(request):
    return render(request, 'custom/contact.html', {})


def about(request):
    return render(request, 'custom/about.html', {})

def events(request):
    events = Event.objects.all()
    # upcoming = [event for event in events if event.upcoming]
    return render(request, 'custom/events.html', {'events': events})

def events_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'custom/events-detail.html', {'event': event})
