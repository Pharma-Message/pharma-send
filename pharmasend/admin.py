from django.contrib import admin
from accountforms.models import Doctor, Pharmacist, Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'password', 'is_admin', 'puser', 'duser')
    search_fields = ('username', 'email')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Doctor)
admin.site.register(Pharmacist)
admin.site.register(Account, AccountAdmin)