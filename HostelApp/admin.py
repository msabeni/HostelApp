from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Matron)
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Room)
