# main/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact, Event, GalleryImage

# Main Page View
# def index(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ContactForm()

#     events = Event.objects.order_by('-date')[:3]  # Limit to 3 latest events
#     images = GalleryImage.objects.all()

#     return render(request, 'main/index.html', {
#         'form': form,
#         'events': events,
#         'images': images,
#     })

#from django.shortcuts import render



def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()

    events = Event.objects.order_by('-date')[:3]  # Limit to 3 latest events
    images = GalleryImage.objects.all()

    return render(request, 'main/index.html', {
        'form': form,
        'events': events,
        'gallery_images': images,
    })

# Event Detail View
def events_list(request):
    events = Event.objects.order_by('-date')  # Get all events, sorted by newest first
    return render(request, 'main/events_list.html', {'events': events})