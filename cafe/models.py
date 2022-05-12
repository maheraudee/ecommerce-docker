from distutils.command.upload import upload
from email import message
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.timezone import datetime, now

# Create your models here.
import datetime

from django.db.models.fields.related import ForeignKey

def increment_booking_number():
  last_booking = Order.objects.all().order_by('id').last()
  if not last_booking:
    return str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '0000'
  oid = last_booking.oid
  booking_int = int(oid[9:13])
  new_booking_int = booking_int + 1
  new_oid =  str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(new_booking_int).zfill(4)
  return new_oid

class Order(models.Model):
    oid = models.CharField(max_length = 20, default = increment_booking_number, editable=False)
    # oitem = models.ManyToManyField(to='Item')
    customer = ForeignKey('Customer',on_delete=models.CASCADE, default='')
    worker = ForeignKey('Worker',on_delete=models.CASCADE, default='', blank=True, null=True)
#     odate = models.DateField( blank=True, default=datetime.datetime.now().date())
    odate = models.DateField( blank=True, auto_now=False,auto_now_add=False, )
#     otime = models.TimeField( blank=True, default=datetime.datetime.now().time())
    otime = models.TimeField( blank=True, auto_now=False,auto_now_add=False)
    iotem = models.ManyToManyField(to='Item')
    status_list = [
      ('queued','queued'),
      ('serving', 'serving'),
      ('ready', 'ready')
    ]
    status = models.CharField(max_length=10,default='queued', choices=status_list)
 
    total_price = models.FloatField(default=0)
    
    def __str__(self):
        return self.customer.fname + ' ' + self.oid
def image_upload(instance, filename):
      imagenaeme , extention = filename.split(".")
      return "Items/%s.%s"%( instance.id, extention)

def worker_image_upload(instance, filename):
      imagenaeme , extention = filename.split(".")
      return "Worker/%s.%s"%( instance.ssn, extention)

class Item(models.Model):
      title = models.CharField(default='', max_length=15)
      ingredients = models.TextField(default='', max_length=1000)
      price = models.IntegerField(default=0)
      image = models.ImageField(upload_to=image_upload, default='')
#       status_list = [
#       ('Breakfast','Breakfast'),
#       ('Lunch', 'Lunch'),
#       ('Dinner', 'Dinner')
#     ]
#       status = models.CharField(max_length=10,default='Breakfast', choices=status_list)
      # imenu= models.ManyToManyField(to='Menu', blank=True)
      def __str__(self):
            return self.title

class Menu(models.Model):
      title = models.CharField(max_length=50, default='')
      mitem = models.ManyToManyField(to=Item)
      code_list = [
      ('Breakfast','Breakfast'),
      ('Lunch', 'Lunch'),
      ('Dinner', 'Dinner')
    ]
      code = models.CharField(max_length=10,default='Breakfast', choices=code_list)
      # imenu= models.ManyToManyField(to='Menu', blank=True)
      # mmanager = models.ForeignKey('Manager',on_delete=models.DO_NOTHING, default='')
      
      def __str__(self):
            return self.title

class Person(models.Model):
      ssn = models.CharField(primary_key=True, default='', max_length=10)
      fname = models.CharField( max_length=50,default='')
      lname = models.CharField( max_length=50, default='')
      address = models.CharField( max_length=100, default='')
      telephone = models.CharField( max_length=10, default='')
      def __str__(self):
            return self.fname +'_' + self.lname +'_' + self.ssn
          
class Worker(Person):
      salary = models.FloatField(default=1500)
      image = models.ImageField(upload_to=worker_image_upload, default='')
# class Manager(Person):
#       pass
      # dob = models.DateField()
      
      
class Customer(models.Model):
      fname = models.CharField( max_length=50,default='')
      lname = models.CharField( max_length=50, default='')
      address = models.CharField( max_length=100, default='', blank=True)
      telephone = models.CharField( max_length=10, default='')
      email = models.EmailField(max_length=254,blank=True, null=True) #null=True Django will store empty values as NULL in the database , blank=True the field is allowed to be blank
      def __str__(self):
            return self.fname +'_' + self.lname +'_' + self.telephone



class Reserve(models.Model):
      name = models.CharField(max_length = 100,default='')
      email = models.EmailField(max_length=150,default='')
      message = models.TextField(max_length=500, default='')
      date = models.DateField( auto_now=False, auto_now_add=False)
      time = models.TimeField(auto_now=False, auto_now_add=False)
      
      nperson = models.IntegerField( default=1)
      def __str__(self):
            return self.name