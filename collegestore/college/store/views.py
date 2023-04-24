from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import bio


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bio')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'relo.html')


def demo(request):
    if request.method == 'POST':
        name = request.POST['txt']
        Email = request.POST['email']
        password = request.POST['pswd']
        cp = request.POST['cpswd']
        if password == cp:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=name, email=Email, password=password)
                user.save()
        else:
            messages.info(request, 'Password mismatching')
            return redirect('register')
    return render(request, 'relo.html')


def detail(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        DOB = request.POST.get('DOB', )
        Age = request.POST.get('Age', )
        Gender = request.POST.get('Gender', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        department = request.POST.get('department', )
        material = request.POST.getlist('material', )
        bio1 = bio(name=name, DOB=DOB, Age=Age, Gender=Gender, phone=phone, email=email, address=address,
                   department=department, material=material)
        bio1.save()

        messages.info(request, 'successfully submitted')
    return render(request, 'bio.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
