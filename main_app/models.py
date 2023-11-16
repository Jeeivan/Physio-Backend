from django.db import models
from datetime import date
from django.contrib.auth.models import User

# area = (
#   ('low back'),('neck'),('shoulder'),('elbow'),('wrist'),('hand'),('hip'),('knee'),('ankle/foot')
# )
area = (
    ('low back', 'Low Back'),
    ('neck', 'Neck'),
    ('shoulder', 'Shoulder'),
    ('elbow', 'Elbow'),
    ('wrist', 'Wrist'),
    ('hand', 'Hand'),
    ('hip', 'Hip'),
    ('knee', 'Knee'),
    ('ankle/foot', 'Ankle/Foot')
)


# Create your models here.
class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  def __str__(self):
    return f'{self.name} ({self.id})'
  
class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  def __str__(self):
    return f'{self.name} ({self.id})'

class Bird(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  def __str__(self):
    return f'{self.name} ({self.id})'
  
class Physio_Form(models.Model):
  date = models.DateField()
  body_part = models.CharField(
    max_length = 10,
    choices= area,
    default=area[0]
  )
  time = models.IntegerField("Length of time of condition (months)")
  trauma = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  scans = models.CharField(max_length=100)
  aggs = models.CharField(max_length=100)
  eases = models.CharField(max_length=100)
  past_treatment = models.CharField(max_length=100)
  medication = models.CharField(max_length=100)
  work = models.CharField(max_length=100)
  goals = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Treatment(models.Model):
  date = models.DateField()
  response = models.CharField()
  physio_form_id = models.ForeignKey(Physio_Form, on_delete=models.CASCADE)