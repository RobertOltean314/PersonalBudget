from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('update_profile/', views.update_profile, name='update-profile'),
    path('profile/', views.profile, name='profile'),
    path('reset-password/', views.reset_password, name='reset-password'),

]
