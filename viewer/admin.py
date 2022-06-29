from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from viewer.models import User
from viewer.models import Pictures
from viewer.models import AccountTiers

class UserAdminConfig(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('acc_tier',)}),
    )

admin.site.register(User, UserAdminConfig)
admin.site.register(Pictures)
# admin.site.register(AccountTiers)
# Register your models here.
