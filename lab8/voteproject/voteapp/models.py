from django.db import models

class Vote(models.Model):
    OPTION_CHOICES = [
        ('Good', 'Good'),
        ('Satisfactory', 'Satisfactory'),
        ('Bad', 'Bad'),
    ]

    choice = models.CharField(max_length=20, choices=OPTION_CHOICES)