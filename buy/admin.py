from django.contrib import admin
from .models import Buy

class BuyAdmin(admin.ModelAdmin):
  list_display =('name','price','stock')

admin.site.register(Buy,BuyAdmin)