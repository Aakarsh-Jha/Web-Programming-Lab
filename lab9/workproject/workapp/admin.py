from django.contrib import admin

# Register your models here.
from django.contrib import admin
from workapp.models import Works, Lives

admin.site.register(Works)
admin.site.register(Lives)