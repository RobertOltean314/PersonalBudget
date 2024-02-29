# transactions/signals.py
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Transaction
from budget.models import Budget


@receiver(post_delete, sender=Transaction)
def update_budget_on_transaction_delete(sender, instance, **kwargs):
    # Get the related budget
    budget = Budget.objects.get(user=instance.user)

    # Update total_expenses or total_income based on the transaction type
    if instance.amount_type == 'expenses':
        budget.total_expenses -= instance.amount
    elif instance.amount_type == 'income':
        budget.total_income -= instance.amount

    # Recalculate current_balance
    budget.update_balance()
