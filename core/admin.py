from django.contrib import admin
from .models import Cause, Event, ImageUpload, Trustee, ManagementStaff

# Register your models here.
admin.site.register(Cause)
admin.site.register(Event)
admin.site.register(ImageUpload)
admin.site.register(ManagementStaff)
admin.site.register(Trustee)
