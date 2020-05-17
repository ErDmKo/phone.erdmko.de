from datetime import datetime
from django.db import models

class Phone(models.Model):
    number = models.CharField(
        'Номер телефона',
        max_length=200,
        unique=True
    )
    create_date = models.DateTimeField(
        'date published',
        default=datetime.now,
        blank=True
    )

    def __str__(self):
        return self.number

class TrustQuestion(models.Model):
    phone = models.OneToOneField(
        Phone,
        on_delete=models.CASCADE,
        primary_key=True
    )
    yes = models.IntegerField('да')
    no = models.IntegerField('нет')

    def __str__(self):
        return f'Moжно ли доверять {self.phone.number} номеру'