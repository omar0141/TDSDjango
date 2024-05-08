from django.db import models


class CustomUserPermissions(models.Model):
    class Meta:
        permissions = (
            ("admin", "Can view all data"),
            ("owner", "Can view owner data only"),
            ("customer", "Can view customer data only"),
        )
