from datetime import datetime

from django import forms

from .models import Transaction


class TransactionForm(forms.ModelForm):
    # Additional field for displaying the date in the form
    display_date = forms.DateField(initial=datetime.now().date(), widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Transaction
        # Fields to display in the form
        fields = ['date', 'description', 'amount', 'amount_type', 'category']
        # Customizing widgets for better UI representation
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'amount': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the amount of money you want'}),
            'amount_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        # Setting initial value for the date field
        self.fields['date'].initial = datetime.now().date()


class TransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'description', 'amount', 'amount_type', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'amount': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the amount of money you want'}),
            'amount_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
