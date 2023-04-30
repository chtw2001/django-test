from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import User

def signup_view(request):
    if request.method == 'GET':
        form = UserCreationForm
        context = {'form': form}
        return render(request, 'users/signup.html', context)
    else:
        pass
