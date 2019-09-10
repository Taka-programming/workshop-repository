from django.core.mail import send_mail

subject = "スマートキー通知"
message="スマートキー通知です。"
from_email = "hogehoge@gmail.com"
recipient_list = ["fugafuga@gmail.com"]

recent_record = Distance.objects.raw("SELECT distance, MAX(date) FROM distance")

if recent_record.distance > 10.0:
    send_mail(subject,message,from_email,recipient_list)
