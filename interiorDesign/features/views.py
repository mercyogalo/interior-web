from django.shortcuts import render
from . models import Agent, Service, Hero_section

# Create your views here.
def landing_page(request):
    agents=Agent.objects.all()
    services=Service.objects.all()
    hero_section=Hero_section.objects.all()
    context={
        'agents': agents,
        'services':services,
        'hero_section':hero_section
    }
    return render(request,'index.html', context)

def about(request):
    return render(request,'about.html')

def agents(request):
    return render(request,'agents.html')

def services(request):
    return render(request,'services.html')

def properties(request):
    return render(request,'properties.html')

def contact(request):
    return render(request,'contact.html')

def service_details(request):
    return render(request,'service-details.html')