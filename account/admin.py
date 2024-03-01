from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User, UserType
from account.forms import MyUserChangeForm, MyUserCreationForm


# Register your models here.
# admin.site.register(Restaurant)
# @admin.register(MyUser)
# class MyUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'status')


# @admin.register(MyUser)
# class MyUserTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'type')


class UserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    fieldsets = (
        ('Additional info', {'fields': ('email', 'password', 'phone',)}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('status', {'fields': ('is_staff', 'status',)}),
        ('Важные даты', {'fields': ('birth_date',)})
    )
    list_display = ['email', 'is_staff', ]
    list_filter = ['is_staff', 'is_superuser', ]
    ordering = ('email',)


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    ordering = ('type',)


admin.site.register(User, UserAdmin)
admin.site.register(UserType, UserTypeAdmin)
