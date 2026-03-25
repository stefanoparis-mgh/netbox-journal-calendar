from netbox.plugins import NetBoxPlugin

class JournalCalendarConfig(NetBoxPlugin):
    name = 'netbox_journal_calendar'
    verbose_name = 'Journal Calendar'
    description = 'Visualizza le Journal Entries in un calendario filtrabile'
    version = '1.1.0'
    base_url = 'journal-calendar'
    default_settings = {}

config = JournalCalendarConfig
