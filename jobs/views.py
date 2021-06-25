import jobs
from django.shortcuts import render
from .models import Job

def home(request):
  context = {
    'jobs': Job.objects
  }
  return render(request, 'jobs/home.html', context)
