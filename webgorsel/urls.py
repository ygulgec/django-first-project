from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # admin paneli URL'si doğru şekilde dahil ediliyor
    path('', include('main.urls')),  # main uygulamanızın URL'lerini dahil ediyoruz
]
