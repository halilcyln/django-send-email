# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def homePage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        emailmessage = request.POST.get("emailmessage")

        subject = f'Maili gönderen {name}'
        message = f'Message: {emailmessage}\n\nSender Name: {name}\nSender Email: {email}'

        # Gönderen adını ve e-posta adresini birleştirerek kullanın
        from_email = f'{email}'

        try:
            # E-posta başlığını belirleme
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['halilcyln005@gmail.com'], fail_silently=False)
            messages.success(request, "Mesajınız gönderildi. Teşekkür ederiz!")
        except Exception as e:
            messages.error(request, f"Hata oluştu: {e}")

        return redirect('/')  # Ana sayfaya veya başka bir sayfaya yönlendirme

    return render(request, 'index.html')
