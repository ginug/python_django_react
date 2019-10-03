from django.contrib import admin
from .models import Question, Choice

from django.contrib.admin import AdminSite

AdminSite.site_header=r"Robbie's Control Panel"
# Choices are being shown inline
class ChoiceInline(admin.TabularInline):
    model=Choice
    #how many choices do you want to show by default
    extra=3

# Specify the feilds that are options that you want to show on the admin screen
class QuestionAdmin(admin.ModelAdmin):
    model=Question
    list_display=('question_text','pub_date','was_published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']
    #fields = ['pub_date', 'question_text']
    #fieldset allows you to add sets and set headers 
    # [(Set_heading,{'fields':['question_text']}),]
    fieldsets = (
        (None, {
            "fields": [
                'question_text'
            ],
        }),
        ('Date Information', {
            "fields": [
                'pub_date'
            ],
        }),
        
    )
    inlines=[ChoiceInline]
    
#admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)







