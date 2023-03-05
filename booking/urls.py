from . import views
from django.urls import path


urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    # path("make_booking/", views.MakeBooking.as_view(), name="make_booking"),
    path("make_booking/", views.make_booking, name="make_booking"),
    path('my_account', views.view_booking, name='my_account'),
    path('delete/<booking_id>', views.delete_booking, name='delete'),
    # path("edit_booking/", views.EditBooking.as_view(), name="edit_booking"),
    path('edit_booking/<booking_id>', views.edit_booking, name='edit_booking'),
]
