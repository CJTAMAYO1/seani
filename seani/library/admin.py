from django.contrib import admin

from .models import Question , Module

class QuestionInLine(admin.StackedInline):
     model=Question
     extra=3

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['name', 'Description', 'num_questions']
    inlines=[QuestionInLine]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
     list_display=['pk', 'question_text', 'module','correct']
     list_filter=['module']