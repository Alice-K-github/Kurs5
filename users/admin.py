from django.contrib import admin
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "avatar",
        "phone_number",
        "country",
        "is_staff",

    )
