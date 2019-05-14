from django.shortcuts import render, redirect
from core.models import Cause, Event, Trustee, ManagementStaff
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    causes = Cause.objects.all()
    events = Event.objects.all()
    upcoming_events = [e for e in events if e.upcoming]
    trustees = Trustee.objects.all()
    staff = ManagementStaff.objects.all()
    return render(request, 'home/home.html', {'causes': causes, 'events': upcoming_events, 'trustees': trustees, 'staff': staff})


def cause_detail(request, pk):
    cause = Cause.objects.get(pk=pk)
    return render(request, 'custom/cause.html', {'cause': cause})


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sender_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        message = 'Reply to: %s \n \n Sender Name: %s \n \n' %(sender_email, name) + message
        try:
            send_mail(subject, message, sender_email, ['alamalinitiatives@gmail.com'])
            send_mail('Notification from AL-Amal Initiative Website',
                      'You have a new email at alamalinitiaves@gmail.com. Please check it out.',
                      sender_email, ['rewena001@hotmail.com', 'mort87ada@gmail.com', 'ahmadagaie@gmail.com'])
        except:
            pass
        return redirect('/contact-us')
    else:
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
