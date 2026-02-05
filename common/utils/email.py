import sendgrid
from sendgrid.helpers.mail import Mail

from django.conf import settings

def send_email(to, subject, content):
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    # sg.set_sendgrid_data_residency("eu")
    mail = Mail(
        from_email=settings.SENDGRID_VERIFIED_SENDER,
        to_emails=to,
        subject=subject,
        html_content=content
    )
    return sg.send(mail)
