from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'demo/home.html')

def archive(request): # list
    subject_list = Subject.objects.all()
    return render(request, 'demo/archive/archive_list.html', {'subject_list': subject_list, 'numbers':range(4)})


def subject_detail(request, pk):
    subject_detail = get_object_or_404(Subject, pk=pk)
    return render(request, 'demo/archive/archive_single.html', {'subject': subject_detail})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        print(request)
        return redirect('archive')
    else:
        return redirect('login')
