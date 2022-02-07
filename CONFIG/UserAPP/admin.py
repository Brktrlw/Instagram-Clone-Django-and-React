from django.contrib import admin
from .models import ModelUser
from PostAPP.models import ModelPost


admin.site.register(ModelUser)
admin.site.register(ModelPost)
