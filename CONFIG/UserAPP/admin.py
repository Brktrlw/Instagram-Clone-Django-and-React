from django.contrib import admin
from .models import ModelUser
from PostAPP.models import ModelPost
from django.contrib.auth.admin import UserAdmin


admin.site.register(ModelPost)

class CustomAdmin(UserAdmin):
    model        = ModelUser
    list_display = ("username","email")
    fieldsets    =  UserAdmin.fieldsets +(
        ("Profil Fotoğrafı Değiştirme",{
            "fields":["profilePhoto"]
        }),
    )
admin.site.register(ModelUser,CustomAdmin)