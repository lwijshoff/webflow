from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from .models import LunchDay, LunchBooking, Menu
from django.utils import timezone
from django.views.decorators.http import require_POST

@login_required
def booking(request):
    profile = getattr(request.user, 'profile', None)
    if not profile or not getattr(profile, 'lunch_eligible', False):
        raise PermissionDenied("You are not eligible to book lunch.")

    days = list(LunchDay.objects.filter(date__gte=timezone.localdate()).order_by('date')[:21])
    bookings = LunchBooking.objects.filter(user=request.user, day__in=days)
    bookings_map = {b.day_id: b for b in bookings}
    days_with_booking = [(d, bookings_map.get(d.id)) for d in days]

    if request.method == 'POST':
        day_id = request.POST.get('day')
        menu_id = request.POST.get('menu')
        if not day_id:
            return redirect(reverse('lunch:lunch_booking'))
        day = get_object_or_404(LunchDay, pk=day_id)
        menu = None
        if menu_id:
            menu = get_object_or_404(Menu, pk=menu_id)
        booking_obj, created = LunchBooking.objects.update_or_create(
            user=request.user, day=day,
            defaults={'menu': menu}
        )
        return redirect(reverse('lunch:lunch_booking'))

    return render(request, 'lunch_booking.html', {
        'days_with_booking': days_with_booking,
        'lunch_eligible': True,
    })

@require_POST
@login_required
def book_ajax(request):
    profile = getattr(request.user, 'profile', None)
    if not profile or not getattr(profile, 'lunch_eligible', False):
        return JsonResponse({'error': 'not eligible'}, status=403)
    day_id = request.POST.get('day')
    menu_id = request.POST.get('menu')
    if not day_id:
        return JsonResponse({'error': 'missing day'}, status=400)
    day = get_object_or_404(LunchDay, pk=day_id)
    menu = None
    if menu_id:
        menu = get_object_or_404(Menu, pk=menu_id)
    booking_obj, created = LunchBooking.objects.update_or_create(
        user=request.user, day=day,
        defaults={'menu': menu}
    )
    return JsonResponse({'status': 'ok', 'booking_id': booking_obj.id})
