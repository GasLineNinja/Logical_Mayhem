from django.contrib import admin
from project_apps.models import Users, Courses, Labs

# Register your models here.

admin.site.register(Users)
admin.site.register(Courses)
admin.site.register(Labs)
