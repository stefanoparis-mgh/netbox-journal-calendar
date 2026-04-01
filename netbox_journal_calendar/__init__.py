
from netbox.plugins import PluginConfig
from django.utils.translation import gettext_lazy as _

class JournalCalendarConfig(PluginConfig):
    name = 'netbox_journal_calendar'
    verbose_name = _('Journal Calendar')  # <--- Usa _() per la traduzione
    description = _('A visual calendar for Journal entries')
    version = ('2.5.7')
    author = 'Stefano Paris'
    base_url = 'journal-calendar'
    menu = 'navigation.menu'

config = JournalCalendarConfig
