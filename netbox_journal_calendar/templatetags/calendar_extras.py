from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if not isinstance(dictionary, dict):
        return []
    # Prova a recuperare il giorno (sia come int che str)
    return dictionary.get(key) or dictionary.get(str(key)) or []
