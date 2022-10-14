from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
def signup(request):
    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'signup.html', context)
    form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
    