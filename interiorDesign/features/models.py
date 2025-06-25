from django.db import models

# Create your models here.
class Hero_section(models.Model):
    heading=models.CharField(max_length=100)
    subHeading=models.CharField(max_length=200)
    image=models.ImageField( upload_to='heroImage/',default="image1.jpg")
    
    def __str__(self):
        return self.heading

class Service(models.Model):
    heading=models.CharField(max_length=100)
    subHeading=models.CharField(max_length=200)
    image=models.ImageField(upload_to='serviceImage/',default="image1.jpg")


    def __str__(self):
        return self.heading
    
class Team(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='teamsImage/',default="image1.jpg")
    linkedin_url=models.CharField(max_length=1000, default="default.com")


    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name=models.CharField(max_length=50)
    comment=models.CharField(max_length=400)
    image=models.ImageField(upload_to='testimonialImage/',default="image1.jpg")
    

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='portfolioImage/',default="image1.jpg")

    def __str__(self):
        return self.name