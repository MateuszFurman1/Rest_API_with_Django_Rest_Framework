from django.contrib import admin

from movielist.models import Person, Movie

# Register your models here.
admin.site.register(Person)
admin.site.register(Movie)