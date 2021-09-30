from django.contrib import admin

# Register your models here.
from .models import Expence, Income


admin.site.register(Expence)
admin.site.register(Income)
