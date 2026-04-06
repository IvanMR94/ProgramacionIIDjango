from django.db import models
from django.core.validators import RegexValidator

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dni = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(r'^\d{7,8}$')]
    )
    birth_date = models.DateField()

    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name