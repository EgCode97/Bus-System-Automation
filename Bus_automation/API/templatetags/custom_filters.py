from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='is_even')
def is_even(num):
    try:
        return 1 if num % 2 == 0 else 0
    except ZeroDivisionError:
        return 0

@register.filter(name='month_as_str')
def month_as_str(month_num):
    months = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
    }
    return months[month_num]


@register.filter(name='minutes_two_digits')
def minutes_two_digits(minute):
    minute = str(minute)
    return minute if len(minute) > 1 else f"0{minute}"