from django.contrib import admin
from .models import Quiz, Question, Answer
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ['id', 'title', 'topic']
    list_filter = ('topic', )


class AnswerInline(admin.TabularInline):
    model = Answer
    max_num = 10
    min_num = 2
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]
    list_display = ('id', 'text', 'quiz')
    list_display_links = ('id', 'text', 'quiz')
    list_filter = ('quiz', )
    search_fields = ('id', 'quiz')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'is_correct', 'question')
    list_display_links = ('id', 'text', 'is_correct', 'question')
    list_filter = ('question', 'is_correct')
    search_fields = ('id', 'text', 'question')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)