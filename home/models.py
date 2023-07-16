from django.db import models
# class student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerFi
#     email = models.EmailField()
#     address = models.TextField(null = True , blank = True)
#     image = models.ImageField()
#     file = models.FileField()
    
class Car(models.Model):
    car_name =  models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
 
    def __str__(self):
        return self.Car_speed
    

    


# yeh sb shell(terminal) mae krne h
# python manage.py shell
# from shop.models import Product
# products.objects.all()
# myprod=Product(product_name="mouse")
# from django.utils import timezone
# myprod.save()
# myprod.product_name