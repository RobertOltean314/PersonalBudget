from django.urls import path

from budget import views

# TODO O interfata mai frumoasa la budget + un model

app_name = 'budget'

urlpatterns = [
    path('budget/', views.budget_view, name='budget')
]
