from django.contrib import admin

# Register your models here.

from .models import Courses

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name','slug','start_date','created_at']
    search_fields = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Courses,CoursesAdmin)
