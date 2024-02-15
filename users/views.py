from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import logout


def register_view(request):
    # If the request method is POST, we're receiving data (the form)
    if request.method == 'POST':
        # We instantiate the form with the POST data
        form = UserRegistrationForm(request.POST)
        # We check if the form is valid
        if form.is_valid():
            # If the form is valid, we save the user
            form.save()
            # We get the username from the cleaned (validated) data
            username = form.cleaned_data.get('username')
            # We send a success message
            messages.success(request, f'Your account has been created! You are now able to login!')
            # We redirect the user to the login page
            return redirect('users:login')
    else:
        # If the request method is not POST, we're just rendering the form
        form = UserRegistrationForm()
    # We render the form
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    # If the request method is POST, we're logging out the user
    if request.method == 'POST':
        # We log out the user
        logout(request)
        # We redirect the user to the login page
        return redirect('users:login')
    # If the request method is not POST, we're just rendering the page
    return render(request, 'users/logout.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        # Populate the forms with the current user's data
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # Check if both forms are valid
        if u_form.is_valid() and p_form.is_valid():
            # Save the updated user and profile data
            u_form.save()
            p_form.save()
            # Display a success message
            messages.success(request, f'Your account has been updated!')
            # Redirect to the update-profile page
            return redirect('users:update-profile')
    else:
        # Create forms with the current user's data (GET request)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Prepare the context to render the template
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    # Render the update_profile template with the provided context
    return render(request, 'users/update_profile.html', context)


def profile(request):
    # Render the profile template without any context data
    return render(request, 'users/profile.html')
