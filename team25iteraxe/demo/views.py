from django.shortcuts import render, get_object_or_404
from .models import Subject


def index(request): # list
    subject_list = Subject.objects.all()
    return render(request, 'archive_list.html', {'subject_list': subject_list})


def subject_detail(request, pk):
    subject_detail = get_object_or_404(Subject, pk=pk)
    return render(request, 'archive_single.html', {'subject': subject_detail})