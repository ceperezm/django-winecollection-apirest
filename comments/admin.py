from django.contrib import admin

from .models import WineComment, ClientCollectionCommment

admin.site.register(WineComment)
admin.site.register(ClientCollectionCommment)
