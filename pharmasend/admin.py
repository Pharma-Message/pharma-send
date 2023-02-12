from django.contrib import admin
from accountforms.models import Doctor, Pharmacist, Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'password', 'is_admin', 'puser', 'duser')
    search_fields = ('username', 'email')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class PharmacistAdmin(ModelAdmin):
    list_display = ('email', 'clinic', 'name')
    search_fields = ('email', 'name', 'clinic')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Doctor)
admin.site.register(Pharmacist, PharmacistAdmin)
admin.site.register(Account, AccountAdmin)