from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_balance(self):
        self.current_balance = self.total_income - self.total_expenses
        self.save()
