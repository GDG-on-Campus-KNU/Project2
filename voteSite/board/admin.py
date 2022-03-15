from django.contrib import admin
from .models import Board, Choice


class BoardAdmin(admin.ModelAdmin):
    search_fields = ['category','content',]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['board','text','count']

admin.site.register(Board, BoardAdmin)
admin.site.register(Choice, ChoiceAdmin)