from django.contrib import admin
from django.contrib.auth.models import  Group
# Register your models here.
from accounts.models import CustomUser
from import_export import resources,fields
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
class UserResource(resources.ModelResource):

    class Meta:
        model = CustomUser
        exclude = ('groups','last_login','password','user_permissions','is_staff','is_superuser','is_active')
        # fields = ('name','email','dob',)
class ShippingAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = UserResource
    model = CustomUser
    search_fields = ('email',)
    # list_filter = ('dob')


admin.site.register(CustomUser,ShippingAdmin)
admin.site.unregister(Group)