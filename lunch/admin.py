from django.contrib import admin
from .models import LunchDay, LunchBooking, MenuItem, Menu



@admin.register(LunchDay)
class LunchDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'note')
    filter_horizontal = ('menus',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_price')
    filter_horizontal = ('items',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(LunchBooking)
class LunchBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'menu', 'booked_at')
    list_filter = ('day',)
    search_fields = ('user__username', 'user__email')
