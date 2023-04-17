from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ["title"]


class UnitAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course")
    list_display_links = ("id", "title", "course")
    search_fields = ["title"]
    list_filter = ("course", )

class TopicPhotInline(admin.TabularInline):
    model = TopicPhoto
    max_num = 20
    min_num = 0
class TopicAdmin(admin.ModelAdmin):
    inlines = [TopicPhotInline, ]
    list_display = ("id", "title", "unit")
    list_display_links = ("id", "title", "unit")
    search_fields = ["title"]
    list_filter = ("unit",)

class ExamplePhotoInline(admin.TabularInline):
    model = ExamplePhoto
    max_num = 20
    min_num = 0

class ExampleNumberInline(admin.TabularInline):
    model = ExampleNumber
    max_num = 20
    min_num = 0

class ExampleAdmin(admin.ModelAdmin):
    inlines = [ExampleNumberInline, ExamplePhotoInline]
    list_display = ("id", "topic")
    list_display_links = ("id", "topic")
    search_fields = ["text"]
    list_filter = ("topic",)


admin.site.register(Course, CourseAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Example, ExampleAdmin)
admin.site.register(TopicPhoto)
admin.site.register(ExamplePhoto)
admin.site.register(ExampleNumber)
