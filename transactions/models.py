from django.db import models
from django.contrib.auth.models import User

from budget.models import Budget


class Transaction(models.Model):
    # Choices for the type of transaction (income or expenses)
    amount_options = (
        ('income', 'Income'),
        ('expenses', 'Expenses')
    )
    category_options = (
        ('housing', 'Housing'),
        ('utilities', 'Utilities'),
        ('groceries', 'Groceries'),
        ('transportation', 'Transportation'),
        ('health care', 'Health Care'),
        ('others', 'Others')
    )

    # Fields for the transaction model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate each transaction with a user
    date = models.DateTimeField()
    description = models.TextField(max_length=500)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    amount_type = models.CharField(choices=amount_options, max_length=8)
    category = models.CharField(choices=category_options, max_length=14)

    def __str__(self):
        return f"{self.description} - {self.amount}"
