from django.shortcuts import render
from .models import Job


# Creting home here because jobs are the biggest part of the homepage
def home(request):
    jobs = Job.objects
    return render(request, "jobs/home.html", {"jobs": jobs})

