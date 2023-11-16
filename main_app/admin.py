from django.contrib import admin
from .models import Cat, Dog, Bird, Physio_Form, Treatment
# Register your models here.
admin.site.register(Cat)
admin.site.register(Dog)
admin.site.register(Bird)
admin.site.register(Physio_Form)
admin.site.register(Treatment)