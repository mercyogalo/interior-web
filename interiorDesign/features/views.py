from django.shortcuts import render

# Create your views here.
def landing_page(request):
    context={}
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