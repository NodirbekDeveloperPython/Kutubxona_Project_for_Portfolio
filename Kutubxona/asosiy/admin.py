from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields =  ('id', 'ism')
    list_display = ('id', 'ism', 'jins', 'kitob_soni')
    list_display_links = ('id', 'ism')
    list_editable = ('kitob_soni',)
    list_filter = ('jins',)

@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ('nom', 'janr', 'muallif__ism')
    list_display = ('id', 'nom' , 'janr', 'muallif')
    list_display_links = ('id', 'nom')
    list_editable = ('janr',)
    list_filter = ('janr',)

@admin.register(Record)
class RecordAdmin(ModelAdmin):
    search_fields = ('student__ism', 'kitob__nom')
    list_display = ('id', 'student' ,'kitob' ,'qaytardi')
    list_display_links = ('id', 'student')
    list_editable = ('kitob',)
    list_filter = ('qaytardi',)
    autocomplete_fields = ('kitob','student')

@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ('id', 'ism', 'tirik', 'kitob_soni')
    list_display = ('id', 'ism', 'tirik', 'kitob_soni')
    list_display_links = ('id', 'ism')
    list_editable = ('kitob_soni',)
    list_filter = ('tirik',)

# admin.site.register(Student)
# admin.site.register(Kitob)
# admin.site.register(Muallif)
# admin.site.register(Record)