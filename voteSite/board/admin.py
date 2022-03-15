from django.contrib import admin
from .models import Board, Choice


class BoardAdmin(admin.ModelAdmin):
    search_fields = ['category']


admin.site.register(Board, BoardAdmin)

admin.site.register(Choice)