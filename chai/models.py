from django.db import models
from django.utils import timezone

class ChaiVariety(models.Model):
    chai_type_choices = [
        ('ML', 'Masala'),
        ('GR', 'Ginger'),
        ('KL', 'Kiwi'),
        ('PL', 'Plain'),
        ('EL', 'Elaichi')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_images')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=chai_type_choices)
    description = models.TextField(default="This is our newly launched chai", max_length=500)
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

