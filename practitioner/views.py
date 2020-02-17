from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserRegistrationForm, ProfileForm

# Create your views here.
def register(request):
    p_form = ProfileForm(request.POST)
    form = UserRegistrationForm(request.POST)
    context = {'form': form, 'p_form': p_form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.filter(username=username).first()
            p_form.instance.user = user
            p_form.save()
            messages.success(request, f'Your account has been created! You can now login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'practitioner/register.html', context)
