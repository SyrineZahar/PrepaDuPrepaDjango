from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        return render(request, 'authentication/register.html', {'form': form})
