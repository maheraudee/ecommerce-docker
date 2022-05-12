from django.contrib import admin

# Register your models here.
from .models import Order, Item, Menu, Person, Worker, Customer,Reserve
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Person)
admin.site.register(Worker)
admin.site.register(Customer)
admin.site.register(Reserve)
# admin.site.register(Manager)