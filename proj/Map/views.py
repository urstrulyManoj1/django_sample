from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'signup.html')

def terms(request):
    return render(request, 'terms.html')