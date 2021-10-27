from django.contrib import admin

from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_diaplay = ('id', 'name', 'email', 'hire_date')
    # search_field = ('name',)
    # list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)