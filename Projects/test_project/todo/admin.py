from django.contrib import admin
from todo import models

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_dt', 'update_dt']
    search_fields = ['title']
    readonly_fields = ['create_dt', 'update_dt']

admin.site.register(models.Task, TaskAdmin)

