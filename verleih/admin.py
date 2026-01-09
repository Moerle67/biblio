from django.contrib import admin

from .models import Buch, Kategorie, Autor, Regal, Stellplatz, Verleihung, Kunde
# Register your models here.

#admin.site.register(Buch)
admin.site.register(Kategorie)
admin.site.register(Autor)
admin.site.register(Regal)
admin.site.register(Stellplatz)
# admin.site.register(Verleihung)
admin.site.register(Kunde)

@admin.register(Verleihung)
class VerleihungAdmin(admin.ModelAdmin):
    list_filter = ['bis', 'von', 'kunde']
    list_display = ['buch', 'kunde', 'von', 'bis']


@admin.register(Buch)
class BuchAdmin(admin.ModelAdmin):
    list_filter = ['kategorie', 'autor']
    search_fields = ['titel']
    filter_horizontal = ['kategorie']
    list_display = ['titel', 'autor']