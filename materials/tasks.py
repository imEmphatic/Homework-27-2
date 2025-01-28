from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_update_notification(course_id, user_email):
    course = Course.objects.get(id=course_id)
    subject = f"Оппа...Обновление курса: {course.title}"
    message = f'Вау! Курс "{course.title}" был обновлен. Проверьте новые материалы!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
