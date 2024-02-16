from django.urls import path
from transactions import views

app_name = 'transactions'

urlpatterns = [
    # URL patterns for transaction-related views
    path('create_transaction/', views.TransactionCreateView.as_view(), name='create-transaction'),
    path('list_of_transactions/', views.TransactionListView.as_view(), name='list-of-transactions'),
    path('update_transaction/<int:pk>/', views.TransactionUpdateView.as_view(), name='update-transaction'),
    path('delete_transaction/<int:pk>/', views.TransactionDeleteView.as_view(), name='delete-transaction'),
]
