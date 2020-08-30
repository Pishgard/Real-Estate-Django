from django.contrib import admin

from .models import Listings


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','realtor','list_date','is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'list_date','realtor')
    list_per_page = 2

admin.site.register(Listings , ListingAdmin)