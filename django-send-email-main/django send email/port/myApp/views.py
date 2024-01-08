from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def homePage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        emailmessage = request.POST.get("emailmessage")
        
        # Kullanıcının gönderdiği mesaj ve email adresini kendi email adresinize gönder
        subject = 'Konu Başlığı'  # E-posta konu başlığı
        message = f'Mesaj: {emailmessage}\n\nGönderen E-posta: {email}'  # E-posta içeriği
        from_email = ''  # Gönderen e-posta adresi

        send_mail(subject, message, from_email, [''])  # E-postayı gönder

        messages.success(request, "Mesajınız iletildi. Teşekkür ederiz!")

        # Başka bir sayfaya yönlendirme
        return redirect('/')  # 'basari_sayfasi' burada kendi başarı sayfanızın URL'si olmalıdır.

    return render(request, 'index.html')