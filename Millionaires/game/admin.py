from django.contrib import admin
from .models import Question, Answer, UserPoint


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'point')
    list_display_links = ('id', 'question')
    list_editable = ('point',)


@admin.register(Answer)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_id', 'answer', 'right')
    list_display_links = ('id', 'answer')
    list_editable = ('right',)


@admin.register(UserPoint)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
    list_editable = ('score',)



