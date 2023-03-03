from django.contrib import admin
from .models import *
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

# Register your models here.

class RadioTextAdmin(NestedStackedInline):
    model = RadioText
    extra = 0

class CloseQuestionsAdmin(NestedModelAdmin):
   model = CloseQuestions
   inlines = [RadioTextAdmin]



class CloseQuestionsForInlineAdmin(NestedStackedInline):
    model = CloseQuestions
    inlines = [RadioTextAdmin,]
    extra = 0
    

class OpenQuestionsAdmin(NestedStackedInline):
    model = OpenQuestions
    extra = 0





class QuizzesAdmin(NestedModelAdmin):
   model = Quizzes
   inlines = [OpenQuestionsAdmin,CloseQuestionsForInlineAdmin,]


admin.site.register(Quizzes, QuizzesAdmin)
admin.site.register(CloseQuestions, CloseQuestionsAdmin)