from django.contrib import admin

from user.models import User, Mentor, Mentee

# Register your models here.
admin.site.register(User)
admin.site.register(Mentor)
admin.site.register(Mentee)
