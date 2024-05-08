from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Studios(models.Model):
    current_time = timezone.localtime(timezone.now()) + timedelta(hours=2)
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    maximum_daily_capacity = models.IntegerField(
        null=False,
        blank=False,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    add_stamp = models.DateTimeField(blank=False, null=False, default=current_time)
