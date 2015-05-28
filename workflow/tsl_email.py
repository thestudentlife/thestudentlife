from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from website import settings

def assignment_email(sender,receiver,assignment):
    text = get_template('email/assignment_email.txt')
    html = get_template('email/assignment_email.html')
    context = Context({'sender':sender,'receiver':receiver,'assignment':assignment})
    subject = "You have a new assignment from TSL editors!"
    from_email = settings.EMAIL_HOST_USER
    to_email = receiver.email
    text_mail =  text.render(context)
    html_mail = html.render(context)
    msg = EmailMultiAlternatives(subject, text_mail, from_email, [to_email])
    msg.attach_alternative(html_mail, "text/html")
    msg.send(fail_silently=True)
