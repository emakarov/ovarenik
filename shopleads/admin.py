from models import *
from django.contrib import admin

class LeadAdmin(admin.ModelAdmin):
  list_display = ['received','content']

admin.site.register(Lead,LeadAdmin)
