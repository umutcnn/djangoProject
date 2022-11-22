from django.contrib import admin

from Work.models import Category, work


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class workAdmin(admin.ModelAdmin):
    list_display = ['title','category','amount','status']
    list_filter = ['amount']

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(work,workAdmin)