from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


# Create your models here.
class Booking(models.Model):

    ACTIVITY_LIST = (
        ('TBW', 'Team Building Workshop'),
        ('CTC', 'Carnival Team Challenge'),
        ('BBC', 'Bridge Building Challenge'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User name'),
        related_name='bookings',
        blank=True, null=True,
    )

    forename = models.CharField(
        verbose_name=_('First name'),
        max_length=20,
        blank=True,
    )

    surname = models.CharField(
        verbose_name=_('Last name'),
        max_length=20,
        blank=True,
    )

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True,
    )

    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=256,
        blank=True,
    )

    creation_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True,
    )

    total_no_group = models.IntegerField(
        verbose_name=('No. in Group(Min 10, Max = 30)'),
        default=10,
        validators=[
            MaxValueValidator(30),
            MinValueValidator(10)
        ],
        blank=True, null=True,
    )

    activity_type = models.CharField(
        verbose_name=_('Activity Type'),
        default='BBC',
        choices=ACTIVITY_LIST)

    booking_date = models.DateField(
        verbose_name=_('Booking date'),
        blank=True, null=True,
    )

    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        super(Event, self).save(*args, **kwargs)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return (str(self.user))
