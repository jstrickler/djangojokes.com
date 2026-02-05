from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldset_list = list(UserAdmin.fieldsets[1][1]['fields'])
    fieldset_list.append('favorite_color')
    UserAdmin.fieldsets[1][1]['fields'] = tuple(fieldset_list)

