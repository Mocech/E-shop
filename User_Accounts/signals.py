from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.sites.models import Site
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_welcome_email(instance)
    else:
        instance.profile.save()

def send_welcome_email(user):
    subject = 'Moxien Online Shop'
    current_site = Site.objects.get_current()
    homepage_url = f"http://{current_site.domain}{reverse('store:home')}"
    message = f"""
    Hi {user.username},

    Thank you for signing up at our site. Please visit our homepage to explore more.

    {homepage_url}
    """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)
