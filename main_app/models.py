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
class Physio_Form(models.Model):
  date = models.DateField(auto_now_add=True)
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  body_part = models.CharField(max_length=100)
  time = models.CharField(max_length=15)
  trauma = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  scans = models.CharField(max_length=100)
  aggs = models.CharField(max_length=100)
  eases = models.CharField(max_length=100)
  past_treatment = models.CharField(max_length=100)
  medication = models.CharField(max_length=100)
  work = models.CharField(max_length=100)
  goals = models.CharField(max_length=100)
  treatment_complete = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Treatment(models.Model):
  date = models.DateField(auto_now_add=True)
  response = models.CharField()
  physio_form_id = models.ForeignKey(Physio_Form, on_delete=models.CASCADE)

class Discussion(models.Model):
  date = models.DateField(auto_now_add=True)
  message = models.CharField()
  # user = models.ForeignKey(User, on_delete=models.CASCADE)