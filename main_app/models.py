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
  date = models.DateField(auto_now_add=True)
  response = models.CharField()
  physio_form_id = models.ForeignKey(Physio_Form, on_delete=models.CASCADE)