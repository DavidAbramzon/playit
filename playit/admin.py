from django.contrib import admin
from playit.models import Subtitle

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subtitle, AuthorAdmin)