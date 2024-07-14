from django.contrib import admin
from .models import Staff,ActivityLog,User,Order,BannedIP



admin.site.register(User)
admin.site.register(Order)
admin.site.register(BannedIP)
admin.site.register(Staff)
admin.site.register(ActivityLog)

