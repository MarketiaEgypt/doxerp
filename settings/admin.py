from django.contrib import admin

# Register your models here.
from settings.models import Setting, Contact, ClientLogo

admin.site.register(Setting)
admin.site.register(Contact)
admin.site.register(ClientLogo)