from django.contrib import admin
from .models import Todo

# Register your models here.
@admin.register(Todo)
class Todoadmin(admin.ModelAdmin):
    list_display = ['id','task','description','completed']