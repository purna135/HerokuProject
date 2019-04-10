from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.mail import EmailMessage
from smtplib import SMTPException
from .models import Images
from time import gmtime, strftime
from twilio.rest import Client
import os
# Create your views here.


def home(request):
    return render(request, 'index.html')


class ReceiveImages(APIView):
    def post(self, request, format=None):
        file = request.data.get('file')

        date = strftime("%Y-%m-%d", gmtime())
        time = strftime("%H:%M:%S", gmtime())
        obj = Images.objects.create(photo=file, date=date, time=time)
        obj.save()

        send_mail(obj.photo.path)
        whatsapp(obj.photo.url)
        return Response('ok', status=status.HTTP_200_OK)


def send_mail(file):
    tomail = 'purnachandramansingh135@gmail.com'
    subject = 'Security Report'
    message = f'Someone at the door. Do I allow them?'

    mail = EmailMessage(subject, message, to=[tomail])
    mail.attach_file(file)

    try:
        mail.send()
    except (SMTPException, Exception) as e:
        pass


def whatsapp(url):
    account_sid = 'AC2b1baea939fb45460c69fbb078edd61d'
    auth_token = '782fc883c0f6aa914d58204be156460d'
    client = Client(account_sid, auth_token)

    photo_url = f'http://litindia.herokuapp.com{url}'

    message = client.messages \
        .create(
            media_url= photo_url,
            from_='whatsapp:+14155238886',
            body="Someone at the door. Do I allow them?",
            to='whatsapp:+919668838634'
         )
    print(message.sid)