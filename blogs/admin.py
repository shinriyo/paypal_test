from django.contrib import admin

# Register your models here.
from blogs.models import PurchaseHistory

class PurchaseHistoryAdmin(admin.ModelAdmin):
    """Allows the administrator to view and modify uploaded audio files"""
    list_display = ('id', 'name', 'message', 'purchase_date')
    #list_display_links = ['id', 'name',]
    ordering = ('id', )

admin.site.register(PurchaseHistory, PurchaseHistoryAdmin)