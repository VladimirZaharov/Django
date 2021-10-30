from django.contrib import admin

from baskets.models import Basket
# Register your models here.

class BasketAdmin(admin.TabularInLine):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    extra = 0
    readonly_fields = ('created_timestamp',)