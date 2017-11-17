from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import send_email_task

User = get_user_model()


class EmailView(APIView):
    def post(self, request):
        email_list = request.data.getlist('email')
        subject = request.data['subject']
        message = request.data['message']

        for email in email_list:
            send_email_task.delay(
                subject,
                message,
                email,
            )
        return Response(status=status.HTTP_200_OK)
