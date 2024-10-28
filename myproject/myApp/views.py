
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'myApp/home.html')

def education(request):
    return render(request,'myApp/education.html')

def work_experience(request):
    return render(request,'myApp/work_experience.html')

def social_media(request):
    return render(request,'myApp/social_media.html')

def profile(request):
    return render(request,'myApp/profile.html')