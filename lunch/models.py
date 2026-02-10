from django.db import models
from django.contrib.auth.models import User


class LunchDay(models.Model):
    date = models.DateField(unique=True)
    note = models.CharField(max_length=255, blank=True, default='')
    menus = models.ManyToManyField('Menu', related_name='days', blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.date.isoformat()


# --- New Menu and MenuItemInMenu models ---
class Menu(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField('MenuItem', related_name='menus', blank=True)

    def total_price(self):
        return sum([item.price for item in self.items.all()])

    def __str__(self):
        return f"{self.name} (Total: {self.total_price()}€)"


class MenuItem(models.Model):
    """Reusable menu items admins define once and can reuse on days."""
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} ({self.price}€)"

class LunchBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey(LunchDay, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.SET_NULL)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'day')
        ordering = ['-booked_at']

    def __str__(self):
        return f"{self.user.username} booking for {self.day}: {self.menu}"
