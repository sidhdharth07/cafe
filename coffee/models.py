from django.db import models

#  Create your models here.
class background_video(models.Model):
    video=models.FileField(upload_to='static/background')

class cold_coffee(models.Model):
    cold_coffee_image=models.ImageField(upload_to='static/background')
    cold_text=models.CharField(max_length=250)
    price=models.IntegerField()
    caption=models.CharField(max_length=250)

class hot_coffe(models.Model): 
    hot_coffee_image=models.ImageField(upload_to='static/background')
    hot_text=models.CharField(max_length=250)
    hot_price=models.IntegerField()
    hot_caption=models.CharField(max_length=250)

class juice(models.Model):
    jyuice_image=models.ImageField(upload_to='static/background')
    jyuice_name=models.CharField(max_length=250)
    jyuice_price=models.IntegerField()
    jyuice_caption=models.CharField(max_length=250)
# special iteams page
class special_iteams(models.Model):
    special_image=models.ImageField(upload_to='static/background')
    special_text=models.CharField(max_length=250)
    special_price=models.IntegerField()
    special_caption=models.CharField(max_length=250)

class contactbox(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=70)
    message=models.CharField(max_length=500)

class about_page(models.Model):
    tital=models.CharField(max_length=50)
    about_text=models.CharField(max_length=500)
    about_image=models.ImageField(upload_to='static/background')  
    
class about_page_right(models.Model):
    tital=models.CharField(max_length=50)
    about_text=models.CharField(max_length=500)
    about_image=models.ImageField(upload_to='static/background')







    
