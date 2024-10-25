from django.contrib import admin
from .models import (Person, Question, Quiz, Option, QuestionText)


admin.site.register(Person)

admin.site.register(Quiz)
class OptionAdmin(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'id',)
    inlines = [OptionAdmin]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(QuestionText)