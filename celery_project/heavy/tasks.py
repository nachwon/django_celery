from django.core.mail import send_mail

from config import celery_app


@celery_app.task(bind=True)
def send_email_task(self, subject, message, recipient):
    send_mail(
        subject=subject,
        message=message,
        from_email='nachwon@gmail.com',
        recipient_list=[
            recipient,
        ],
    )

