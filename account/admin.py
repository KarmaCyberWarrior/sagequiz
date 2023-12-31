from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import *

# Register your models here.
class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_teacher', 'is_student', 'is_approved')
	search_fields = ('email', 'username', 'first_name', 'last_name')
	readonly_fields = ('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter=()
	fieldsets=()

admin.site.register(Account, AccountAdmin)
admin.site.register(Teacher)
admin.site.register(Student)