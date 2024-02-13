from django.urls import path

from . import views

app_name = 'home_page'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
]
