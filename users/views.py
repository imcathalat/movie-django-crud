from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from movies_uploads import urls

def user_sign(request):
    if request.method == 'GET':
        return render(request, 'registration/sign_in.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse user')
        

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse("usuario cadastrado com sucesso")


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There Was An Error Logging In, Try Again.'))
            return render(request, 'registration/login.html')

    else:
        return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

    
        


