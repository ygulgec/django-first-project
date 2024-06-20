from django.db import models

class Hakkimizda(models.Model):
    content = models.TextField()

class Projeler(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    completed_date = models.DateField()

class Hizmetler(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='services/')

class Bloglar(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='blogs/')
    published_date = models.DateField()

class Iletisim(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
