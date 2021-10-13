from django.shortcuts import render, get_object_or_404
from .models import Subject

def home(request):
    return render(request, 'demo/home.html')

def archive(request): # list
    subject_list = Subject.objects.all()
    return render(request, 'demo/archive/archive_list.html', {'subject_list': subject_list})


def subject_detail(request, pk):
    subject_detail = get_object_or_404(Subject, pk=pk)
    return render(request, 'demo/archive/archive_single.html', {'subject': subject_detail})