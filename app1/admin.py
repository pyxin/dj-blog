from django.contrib import admin

# Register your models here.
from .models import User,Article,Tag,Menu,Catalog
admin.site.register(Article)
admin.site.register(Catalog)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Menu)
