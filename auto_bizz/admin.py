from django.contrib import admin

from .models import daily_bizz
from .models import electricity
from .models import hard_ware

class daily_bizzAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['date_time']}),
        ('Amount earned from', {'fields': ['play_station']}),
        (None,               {'fields': ['flash_mem']}),
        (None,               {'fields': ['comp_repair']}),
    ]
    list_display =  ('date_time','play_station','flash_mem','comp_repair','above_average')

    list_filter = ['date_time']
    search_fields = ['play_station']

class electricity_Use(admin.ModelAdmin):
    fieldsets = [
        ('Electricity reading',  {'fields': ['daily_reading']}),
        (None,                  {'fields': ['weekly_reading']}),
        ('Paid',                  {'fields': ['amt_deposited']}),
        (None,                  {'fields': ['date_time']}),
        ]
    
    list_display =  ('daily_reading','weekly_reading','amt_deposited','date_time')
class my_hardWare (admin.ModelAdmin):
    fieldsets =[
        ('My stuff',  {'fields': ['item']}),
        (None       ,  {'fields': ['price']}),
        (None,     {'fields': ['installation_amt']}),
        ('Purchased on',  {'fields': ['date_time']}),
        ]
    list_display =  ('item','price','installation_amt','date_time')
    list_filter = ['date_time']
    
    
admin.site.register(daily_bizz, daily_bizzAdmin )
admin.site.register(electricity, electricity_Use)
admin.site.register(hard_ware, my_hardWare)



# Register your models here.
