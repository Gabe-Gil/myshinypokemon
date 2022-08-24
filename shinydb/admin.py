from django.contrib import admin
from .models import Shiny

# Register your models here.
class Shiny_Admin(admin.ModelAdmin):
    fields = ['nickname', 'species', 'attempts', 'method', 'date_caught', 'author']
    list_display = ['nickname', 'species', 'method', 'date_caught', 'author']
    list_filter = ['date_caught']
    search_fields = ['nickname']

admin.site.register(Shiny, Shiny_Admin)