from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from Booking.models.studios import Studios


class Reserves(models.Model):
    current_time = timezone.localtime(timezone.now()) + timedelta(hours=2)
    id = models.AutoField(primary_key=True)
    from_date = models.DateField(blank=False, null=False)
    to_date = models.DateField(blank=False, null=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    studio = models.ForeignKey(Studios, on_delete=models.CASCADE, null=False)
    add_stamp = models.DateTimeField(blank=False, null=False, default=current_time)
    cancel = models.DateTimeField(blank=False, null=True)
