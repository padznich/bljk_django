from django.contrib import admin

from models import Summary, Detail, Description

# Register your models here.

admin.site.register([Summary, Description, Detail])
