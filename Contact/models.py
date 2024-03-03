from django.db import models

class ContactDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
