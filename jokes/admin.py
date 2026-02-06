from django.contrib import admin

# Register your models here.
from .models import Joke, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()

@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke
    list_display = ['question', 'answer', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated')
        return ()
