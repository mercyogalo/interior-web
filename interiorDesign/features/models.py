from django.db import models

# Create your models here.
class Hero_section(models.Model):
    heading=models.CharField(max_length=100)
    subHeading=models.CharField(max_length=200)
    image=models.ImageField( upload_to='hero',default="image1.jpg")
    
    def __str__(self):
        return self.heading

class Service(models.Model):
    heading=models.CharField(max_length=100)
    subHeading=models.CharField(max_length=200)


    def __str__(self):
        return self.heading
    
class Agent(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='agents',default="image1.jpg")


    def __str__(self):
        return self.name
    