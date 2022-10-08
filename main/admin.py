from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Songs)
@admin.register(Songs)
class SongsAdmin(ImportExportModelAdmin):
    search_fields=('Artist','SongTitle','Label','LW')
    list_display = ('LW','Artist','SongTitle','Label')
