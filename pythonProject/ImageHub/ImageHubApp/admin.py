from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Images

# Register your models here.
@admin.register(Images)
class Images(admin.ModelAdmin):
    list_display = ('title', 'description', 'view')
    # list_filter = ('id', 'companyName', 'phone', 'address', 'email', 'site')
    # search_fields = ('id', 'companyName', 'phone', 'address', 'email', 'site')

    readonly_fields = ["view"]

    def view(self, obj):
        return mark_safe(f'<img width="200px" src="{obj.image.url}">')