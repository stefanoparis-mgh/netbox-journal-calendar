from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if not dictionary: return []
    # Cerchiamo sia come intero che come stringa per sicurezza
    return dictionary.get(key) or dictionary.get(str(key)) or []
