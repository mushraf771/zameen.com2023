from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect


class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny,)
    # @csrf_protect

    def post(self, request, format=None):
        data = self.request.data
        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                # '[YOUR SENDER EMAIL FROM YOUR SETTINGS]',
                'kiranchm143@gmail.com',
                # ['[EMAIL YOU ARE SENDING TO]'],
                ['kiranchm143@gmail.com'],
                fail_silently=False
            )
            contact = Contact(name=data['name'], email=data['email'],
                              subject=data['subject'], message=data['message'])
            contact.save()
            return Response({'success': ' Your Message sent successfully'})
        except:
            return Response({'error': 'Message Sending Failed'})
