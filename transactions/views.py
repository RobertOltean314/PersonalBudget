from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from transactions.forms import TransactionForm, TransactionUpdateForm
from transactions.models import Transaction
from datetime import datetime


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
        return super().form_valid(form)

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    # View for updating an existing transaction
    template_name = 'transactions/update_transaction.html'
    model = Transaction
    form_class = TransactionUpdateForm
    success_url = reverse_lazy('transactions:list-of-transactions')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    # View for deleting an existing transaction
    template_name = 'transactions/delete_transaction.html'
    model = Transaction
    success_url = reverse_lazy('transactions:list-of-transactions')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
