from django.contrib import admin

# Register your models here.
from .models import Product

admin.site.site_header="buy&sell"
admin.site.site_title="dashborad"
admin.site.index_title="dashborad buy and sell"

class productAdmin(admin.ModelAdmin):
    list_display=('name','price','desc')
    search_fields  =('name',)
    list_editable=('price','desc')

admin.site.register(Product,productAdmin)