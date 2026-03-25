
from netbox.plugins import PluginConfig

class JournalCalendarConfig(PluginConfig): # Usa PluginConfig
    name = 'netbox_journal_calendar'
    verbose_name = 'Journal Calendar'
    description = 'Calendario interattivo per Journal Entries (Device, VM, Service)'
    version = '1.3.7'
    base_url = 'journal-calendar'

config = JournalCalendarConfig
