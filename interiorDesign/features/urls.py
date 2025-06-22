from django.urls import path
from . import views




urlpatterns = [
    path('', views.landing_page, name="landing_page"),
     path('about/', views.about, name="about"),
      path('contact/', views.contact, name="contact"),
       path('properties/', views.properties, name="properties"),
        path('agents/', views.agents, name="agents"),
         path('services/', views.landing_page, name="services"),
          path('serviceDetails/', views.service_details, name="serviceDetails")
          

]
