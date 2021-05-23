from django.contrib import admin
from .models import Site, Page, PageImages

admin.site.register(Site)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uri', 'site')
    list_filter = ('uri', 'site')
    list_per_page = 50

admin.site.register(Page, PageAdmin)

admin.site.register(PageImages)
