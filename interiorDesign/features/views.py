from django.shortcuts import render
from . models import Team, Service, Hero_section, Testimonial, Portfolio,Message
from django.core.mail import send_mass_mail

# Create your views here.
def landing_page(request):
    teams=Team.objects.all()
    services=Service.objects.all()
    hero_section=Hero_section.objects.all()
    testimonials=Testimonial.objects.all()
    portfolios=Portfolio.objects.all()

    if request.method=="POST":
            name=request.POST["name"]
            email=request.POST["email"]
            subject=request.POST["subject"]
            message=request.POST["message"]


            eachMessage=Message(email=email,name=name, subject=subject,message=message)
            eachMessage.save();

            message1 = (
            "Subject here",
            "Here is the message",
            "from@example.com",
            ["first@example.com"],
        )
            message2 = (
            "Another Subject",
            "Here is another message",
            "from@example.com",
            ["second@test.com"],
        )
            send_mass_mail((message1, message2), fail_silently=False)
            


    context={
        'teams': teams,
        'services':services,
        'hero_section':hero_section,
        'testimonials':testimonials,
        'portfolios':portfolios
    }
    return render(request,'index.html', context)
