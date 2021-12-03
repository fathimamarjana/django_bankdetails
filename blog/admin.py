from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *

# Register your models here.
admin.site.register(Bank)
admin.site.register(Public_branches)
admin.site.register(Public_bank_branches)




