from django.contrib import admin
from todo.models import Task
from todo.models import Member
from todo.models import Setting


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'due_date',
        'completed',
        'created_at'
    )


admin.site.register(Task, TaskAdmin)
admin.site.register(Member)
admin.site.register(Setting)