from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Permette di accedere a un dizionario nel template usando una chiave variabile."""
    return dictionary.get(key)
