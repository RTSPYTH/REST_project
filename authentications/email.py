from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def email_send(user):
    context = {
        'text_detail': 'Спасибо за регистрацию',
        'email': user.email,
        'domain': 'http://127.0.0.1:8000/',
        'activation_code': user.activation_code,
    }

    message = render_to_string('email.html', context,)
    plain_message = strip_tags(message)
    subject = 'Активация'
    to_email = user.email
    mail.send_mail(
        subject, plain_message, 'erbolboni222@gmail.com', [to_email,], html_message=message
    )