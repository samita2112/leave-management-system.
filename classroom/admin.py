from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Manager, User,Adminn,Leave
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(Manager)
admin.site.register(Adminn)

