from django.contrib import admin
from .models import Category, Courses

admin.site.site_title = 'Courses admin panel'
admin.site.site_header = 'Courses'
admin.site.index_title = 'Welcome to admin area'


class CoursesInline(admin.TabularInline):
    model = Courses
    exclude = ['created_at']
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Courses, CourseAdmin)
