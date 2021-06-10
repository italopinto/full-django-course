from django.contrib import admin
from .models import Client, ID, Sale, Product


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'age', 'salary', 'dt_birth', 'photos']
    list_filter = ['name', 'last_name', 'age', 'salary', ]
    search_fields = ['last_name', 'age']


class SaleAdmin(admin.ModelAdmin):
    list_display = ['sale_number', 'client', 'date', 'total']
    list_filter = ['sale_number', 'date']
    search_fields = ['sale_number']


admin.site.register(Client, ClientAdmin)
admin.site.register(ID)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Product)
