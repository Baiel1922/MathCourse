from django.contrib import admin
from .models import Quiz, Question, Answer, Submission
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    max_num = 6
    min_num = 2

# class QuestionInline(admin.TabularInline):
#     model = Question
#     max_num = 6
#     min_num = 2

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "question", "is_correct")
    list_display_links = ("id", "text", "question", "is_correct")
    search_fields = ["text", ]
    list_filter = ("question", "is_correct")

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]
    list_display = ("id", "text", "quiz")
    list_display_links = ("id", "text", "quiz")
    search_fields = ["text"]
    list_filter = ("quiz", )

class QuizAdmin(admin.ModelAdmin):
    # inlines = [QuestionInline,]
    list_display = ("id", "title", "topic")
    list_display_links = ("id", "title", "topic")
    search_fields = ["title"]
    list_filter = ("topic",)

admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Submission)

