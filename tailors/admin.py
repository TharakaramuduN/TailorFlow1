from django.contrib import admin
from .models import TailorUser
# Register your models here.
from django.contrib.admin.models import LogEntry

admin.site.register(TailorUser)
