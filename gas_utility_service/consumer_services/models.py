from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('gas_connection', 'Gas Connection'),
        ('leak_repair', 'Leak Repair'),
        ('billing_query', 'Billing Query'),
    
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        # Add more status options as needed
    ]

    type_of_request = models.CharField(max_length=100, choices=REQUEST_TYPES)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submission_date = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField(null=True, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming Django's built-in User model for simplicity
    files = models.FileField(upload_to='service_request_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.type_of_request} - {self.submission_date}"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.get_full_name() if self.user.get_full_name() else self.user.username

