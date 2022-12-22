from django.contrib import admin

from Work.models import Category, work, Images

class WorkImageInline(admin.TabularInline):
    model = Images
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','status']
    list_filter = ['status']

class WorkAdmin(admin.ModelAdmin):
    list_display = ['title','category','amount','image_tag','status']
    list_filter = ['amount']
    inlines = [WorkImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','work','image_tag']


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(work,WorkAdmin)
admin.site.register(Images,ImagesAdmin)