from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import logout

# TODO Vezi cum functioneaza register function si cum sa faci user care sa se inregistreze

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('login')
#     return render(request, 'users/logout.html')
