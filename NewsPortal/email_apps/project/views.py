from django.shortcuts import render, redirect
from django.core.mail import send_mail, mail_admins, mail_managers, EmailMultiAlternatives
from datetime import datetime
from django.views import View
from .models import Appointment

from allauth.account.signals import user_signed_up
from django.dispatch import receiver



class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'project/index.html')

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )

        appointment.save()

        # Подключаем к нашему emaily
        send_mail(
            subject=f'{appointment.client_name}: {appointment.date.strftime("%Y-%m-%d")}',
            message=appointment.message,
            from_email='imaralievasadbek@yandex.ru',
            recipient_list=['imaraliev.kg2005@gmail.com'],
        )

        return redirect('appointment:project/index')



@receiver(user_signed_up)
def send_welcome_email(sender, request, user, **kwargs):
    subject = 'Добро пожаловать в News Portal!'
    message = 'Спасибо за регистрацию на News Portal. Надеемся, вам понравится наше содержание.'
    from_email = 'your_email@example.com'  # Замените на свой email
    to_email = [user.email]
    send_mail(subject, message, from_email, to_email, fail_silently=False)


