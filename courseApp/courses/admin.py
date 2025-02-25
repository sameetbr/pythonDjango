from django.contrib import admin
from .models import Course, Categories

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive", "slug")
    list_display_links = ("title","slug",)
    list_editable = ("isActive",)
    list_filter = ("title", "isActive",)
    readonly_fields = ("slug",)
    search_fields = ("title", "slug",)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    readonly_fields = ("slug",)
    list_display_links = ("name","slug",)