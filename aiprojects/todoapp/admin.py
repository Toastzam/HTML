from django.contrib import admin
from .models import Todo, Question


# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    search_fields = ['todo']


admin.site.register(Todo, TodoAdmin)


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
