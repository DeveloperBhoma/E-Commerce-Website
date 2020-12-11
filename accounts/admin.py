from django.contrib import admin

# Register your models here.
from .models import *  #yaani models se maangaa hai ki tumaahaare paas hai jo hme de do.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)