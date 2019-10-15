from django.contrib import admin

from . models import Level
from . models import EnglishWords


class WordAdmin(admin.ModelAdmin):
    list_display = ('En_Word', 'Bn_Word', 'En_Trans', 'Bn_Trans', 'Level', 'date')


admin.site.register(EnglishWords, WordAdmin)
admin.site.register(Level)
