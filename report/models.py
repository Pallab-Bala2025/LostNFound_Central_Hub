from django.db import models
from django.contrib.auth.models import User

class ItemReport(models.Model):
    REPORT_TYPES = (
        ('lost', 'lost'),
        ('found', 'Found'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who submits
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    phone_number = models.CharField(max_length=15)
    report_type = models.CharField(max_length=5, choices=REPORT_TYPES)
    image = models.ImageField(upload_to='item_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({self.report_type})"
