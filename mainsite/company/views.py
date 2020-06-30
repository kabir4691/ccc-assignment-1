from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'company/index.html')

def contactUs(request):
  return render(request, 'company/contact-us.html')

def contactUsSubmit(request):
  return render(request, 'company/contact-us-submit.html')

def team(request):
  return render(request, 'company/team.html')

