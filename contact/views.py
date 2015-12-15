from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from forms import ContactView
from django.core.mail import EmailMessage


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            email = EmailMessage()
            email.from_email = form.cleaned_data.get('email')
            email.to = [request.POST.get('email')]
            email.topic = form.cleaned_data.get('topic')
            email.body = form.cleaned_data.get('message')

            data = EmailMessage()
            data.from_email = form.cleaned_data.get('email')
            data.to = ['aoifemcevoy@gmail.com']
            data.topic = 'form received'
            data.body = 'message'

            my_form = form.save(commit=False)
            my_form.save()
            messages.add_message(request, messages.INFO, 'Your message has been sent. Thank you.')
            email.send()
            data.send()
            return HttpResponseRedirect('/')
    else:
        form = ContactView()

    return render(request, 'contact.html', {'form': form})
