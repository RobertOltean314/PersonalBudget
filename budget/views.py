from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Budget

@login_required
def budget_view(request):
    budget = Budget.objects.get(user=request.user)
    return render(request, 'budget/budget.html', {'budget': budget})
