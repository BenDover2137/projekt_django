from django.db import models
from django.conf import settings
# Create your models here.
class Zgloszenie(models.Model):
    STATUS_CHOICES = [
        ('open', 'Otwarte'),
        ('progress', 'W trakcie'),
        ('closed', 'Zamknięte'),
    ]
    title = models.CharField(max_length=70)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"


class Odpowiedz(models.Model):
    ticket = models.ForeignKey(Zgloszenie, on_delete=models.CASCADE)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username} - {self.ticket.title}"
