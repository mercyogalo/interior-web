from django.contrib import admin
from . models import Team, Service, Hero_section, Testimonial, Portfolio

# Register your models here.

admin.site.register(Team)
admin.site.register(Service)
admin.site.register(Hero_section)
admin.site.register(Testimonial)
admin.site.register(Portfolio)