from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Choice2

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Choice2)