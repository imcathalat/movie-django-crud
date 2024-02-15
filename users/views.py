from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(username)

    # if user is not None:
    #     login(request, user)
    #     print('user')
    #     return redirect('home')
        
    # else:
    #     messages.success(request, ('There Was An Error Logging In, Try Again.'))
    #     print('primeiro else')
    
        


