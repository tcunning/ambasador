from django.contrib import admin

from django.contrib import admin
from .models import Referral

class ReferralAdmin(admin.ModelAdmin):
    fields = ['name', 'count']		# Fields order
    list_display = ('name', 'count')
    search_fields = ['name']

admin.site.register(Referral, ReferralAdmin)
