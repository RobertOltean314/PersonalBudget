from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from transactions.forms import TransactionForm, TransactionUpdateForm
from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import View
from transactions.models import Transaction, Budget


class TransactionListView(LoginRequiredMixin, ListView):
    # View for listing all transactions
    template_name = 'transactions/list_of_transactions.html'
    model = Transaction
    form_class = TransactionForm
    context_object_name = 'all_transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    # View for creating a new transaction
    template_name = 'transactions/create_transaction.html'
    model = Transaction
    form_class = TransactionForm
    success_url = reverse_lazy('transactions:list-of-transactions')

    def get_initial(self):
        # Set initial values for form fields
        initial = super().get_initial()
        initial['month'] = datetime.now().month
        return initial

    def form_valid(self, form):
        # Automatically associate the transaction with the logged-in user
        form.instance.user = self.request.user
        # Set the month based on the display date
        form.instance.month = form.cleaned_data['display_date'].month

        # Update the budget based on the transaction type
        if form.instance.amount_type == 'income':
            self.request.user.budget.total_income += form.instance.amount
        elif form.instance.amount_type == 'expenses':
            self.request.user.budget.total_expenses += form.instance.amount

        # Recalculate the budget's current balance
        self.request.user.budget.update_balance()

        return super().form_valid(form)

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    # View for updating an existing transaction
    template_name = 'transactions/update_transaction.html'
    model = Transaction
    form_class = TransactionUpdateForm
    success_url = reverse_lazy('transactions:list-of-transactions')

    def form_valid(self, form):
        # Automatically associate the transaction with the logged-in user
        form.instance.user = self.request.user

        # Get the original transaction amount before the update
        original_amount = self.get_object().amount

        # Update the budget based on the transaction type
        if form.instance.amount_type == 'income':
            self.request.user.budget.total_income += (form.instance.amount - original_amount)
        elif form.instance.amount_type == 'expenses':
            self.request.user.budget.total_expenses += (form.instance.amount - original_amount)

        # Recalculate the budget's current balance
        self.request.user.budget.update_balance()

        return super().form_valid(form)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    # View for deleting an existing transaction
    template_name = 'transactions/delete_transaction.html'
    model = Transaction
    success_url = reverse_lazy('transactions:list-of-transactions')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class ResetBudgetView(View):
    def post(self, request, *args, **kwargs):
        # Get the current user's budget
        user_budget = Budget.objects.get(user=request.user)

        # Delete all transactions associated with the user
        Transaction.objects.filter(user=request.user).delete()

        # Update budget totals
        user_budget.total_income = 0
        user_budget.total_expenses = 0
        user_budget.update_balance()

        # Display a success message
        messages.success(request, 'Budget reset successfully!')

        return redirect('transactions:list-of-transactions')  # Redirect to the transactions list page
