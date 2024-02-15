from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    print("aaaaaaaaaaaaaa")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print('user')
            return redirect('home')
            
        else:
            messages.success(request, ('There Was An Error Logging In, Try Again.'))
            print('primeiro else')
            return redirect('login')
    else:
        print('caiu no segundo else')
        return render(request, 'registration/login.html')
        


