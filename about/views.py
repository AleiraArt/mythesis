from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def about(request):
    return render(request, 'about/about.html')

def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully.')
            form = ContactForm()  # clear form after successful submission
    else:
        form = ContactForm()

    return render(request, 'about/about.html', {'form': form})