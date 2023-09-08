from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import LoginForm
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            request.session['user_authenticated'] = True
            return redirect('generate_token')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




def generate_token_view(request):
    if request.session.get('user_authenticated'):
        user = request.user
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key})
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to the login page
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})