from django.contrib import admin

from .models import Part, Category, WorkDescription

admin.site.register(Part)
admin.site.register(Category)
admin.site.register(WorkDescription)
