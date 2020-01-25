from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        # do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # Send email
        send_mail(
            'Contact From Website from: ' + message_name, #subject
            message, #message
            message_email, #from email
            ['andrevan_wyk@hotmail.com'], #to email
            fail_silently=True,
        )



        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})

