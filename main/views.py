from django.shortcuts import render
from .models import Hakkimizda, Projeler, Hizmetler, Bloglar, Iletisim
from django.core.mail import send_mail
from .forms import ContactForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    hakkimizda = Hakkimizda.objects.all()
    return render(request, 'main/about.html', {'hakkimizda': hakkimizda})

def projects(request):
    projeler = Projeler.objects.all()
    return render(request, 'main/projects.html', {'projeler': projeler})

def services(request):
    hizmetler = Hizmetler.objects.all()
    return render(request, 'main/services.html', {'hizmetler': hizmetler})

def blog(request):
    bloglar = Bloglar.objects.all()
    return render(request, 'main/blog.html', {'bloglar': bloglar})

def contact(request):
    iletisim = Iletisim.objects.all()
    return render(request, 'main/contact.html', {'iletisim': iletisim})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form verilerini işleme
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # E-postayı gönderme (Django ayarlarınızda e-posta yapılandırmasının doğru olduğundan emin olun)
            send_mail(
                f'Contact Form Submission from {name}',
                message,
                email,
                ['your-email@example.com'],  # Bu adresi kendi e-posta adresinizle değiştirin
            )

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'main/contact_success.html')