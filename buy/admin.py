from django.contrib import admin
from .models import Buy,Register

class BuyAdmin(admin.ModelAdmin):
  list_display =('name','price','stock')

class RegisterAdmin(admin.ModelAdmin):
  list_display =('username','password','email','phone')

admin.site.register(Buy,BuyAdmin)
admin.site.register(Register,RegisterAdmin)
