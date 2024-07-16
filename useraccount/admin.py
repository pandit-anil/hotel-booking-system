from django.contrib import admin
from .models import User

# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserChange(UserAdmin):

        add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","first_name","last_name", "email", "mobile_no", "address", "password", "profile","document" , "is_staff",
                "is_active", "groups", "user_permissions"
            ),
        }),
            )

