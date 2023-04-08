from django.contrib import admin
 
# Register your models here.
from .models import Question, Choice
 
class ChoiceInLine(admin.StackedInline):
    model = Choice 
    extra = 3
  
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
 
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)