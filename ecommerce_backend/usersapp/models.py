from django.db import models

# Create your models here.


# Register & Login models created

class users(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    email=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=10,null=False)
    

# home products models created

class products(models.Model):
    title=models.CharField(max_length=100)
    price=models.CharField(max_length=200)
    description=models.TextField()
    image=models.URLField(default="empty")  