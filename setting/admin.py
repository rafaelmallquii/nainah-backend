from django.contrib import admin
from .models import Setting, SiteMeta

class InlineSiteMeta(admin.StackedInline):
    model = SiteMeta
    extra = 1

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    inlines = [InlineSiteMeta,]
    list_display = ('site_name', 'site_description', 'site_logo')