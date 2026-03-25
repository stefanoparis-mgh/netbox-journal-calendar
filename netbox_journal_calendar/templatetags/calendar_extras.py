from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    # Restituisce una lista vuota se la chiave non esiste nel dizionario
    if dictionary is None:
        return []
    return dictionary.get(key, [])
