from django import template
from django.utils import formats
from django.utils.translation import get_language
import datetime

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if not isinstance(dictionary, dict): return []
    return dictionary.get(key) or dictionary.get(str(key)) or []


@register.filter
def get_day_name(day_index):
    try:
        reference_monday = datetime.date(2024, 1, 1)
        target_day = reference_monday + datetime.timedelta(days=int(day_index))
        return formats.date_format(target_day, "D")
    except Exception:
        return ""

@register.filter
def get_day_abbr_from_index(index):
    try:
        day_of_week = int(index) % 7
        reference_monday = datetime.date(2024, 1, 1)
        target_day = reference_monday + datetime.timedelta(days=day_of_week)
        return formats.date_format(target_day, "D").upper()
    except:
        return ""