
from netbox.plugins import PluginConfig

class JournalCalendarConfig(PluginConfig): # Usa PluginConfig
    name = 'netbox_journal_calendar'
    verbose_name = 'Journal Calendar'
    description = 'Calendario per Journal Entries'
    version = '1.2.9'
    base_url = 'journal-calendar'

config = JournalCalendarConfig
