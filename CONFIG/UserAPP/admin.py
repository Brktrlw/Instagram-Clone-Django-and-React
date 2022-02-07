from django.contrib import admin
from .models import ModelUser,ModelFollower
from PostAPP.models import ModelPost
from django.contrib.auth.admin import UserAdmin

@admin.register(ModelPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user","unique_id","createdDate"]  # admin tablosunda yazar ve olusturma tarihini göstermesini sağlar
    list_display_links = ["user",]                     # olusturma tarihine de link verir
    search_fields = ["user"]                           # admin sayfasına arama cubugu ekler ve user bilgisine göre arama yaptırır
    list_filter = ["createdDate"]                      # sağ tarafa "Süz" filtreleme işlemi yapan yeri getirir
    class Meta:
        model = ModelPost

class CustomUserAdmin(UserAdmin):
    model        = ModelUser
    list_display = ("username","email")
    fieldsets    =  UserAdmin.fieldsets +\
                    (
        ("Profil Fotoğrafı Değiştirme",{
            "fields":["profilePhoto"],
        }),
        ("Gizlilik Durumu", {
            "fields": ["private"],
        })
    )
admin.site.register(ModelUser,CustomUserAdmin)
admin.site.register(ModelFollower)
