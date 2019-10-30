from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

#class CustomUserAdmin(admin.ModelAdmin): //사용자가 정의한 UserAdmin을 사용함.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields" : (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "currency",
                    "birthdate",
                 )
            }
        ),
    )