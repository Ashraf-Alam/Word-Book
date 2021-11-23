from django.contrib import admin

#Model access into admin section

from . models import Word_Mng

admin.site.register(Word_Mng)