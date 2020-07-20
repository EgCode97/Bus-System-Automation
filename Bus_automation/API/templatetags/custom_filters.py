from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='is_even')
def is_even(num):
    try:
        return 1 if num % 2 == 0 else 0
    except ZeroDivisionError:
        return 0