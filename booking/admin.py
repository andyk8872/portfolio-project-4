from django.contrib import admin
from .models import Booking, Review

# Register your models here.


@admin.register(Booking)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_no_group', 'creation_date', 'approved')
    list_filter = ('approved', 'booking_date')
    search_fields = ('forename', 'surname')


@admin.register(Review)
class Review(admin.ModelAdmin):
    """
    Displays the fields needed in admin page from Review model
    """
    list_display = (
        'user',
        'approved',
        'created_on',
        'review'
    )