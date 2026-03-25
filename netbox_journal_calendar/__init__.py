from netbox.plugins import NetBoxPlugin

class JournalCalendarConfig(NetBoxPlugin):
    name = 'netbox_journal_calendar'
    verbose_name = 'Journal Calendar'
    description = 'Visualizza le Journal Entries in un calendario'
    version = '1.0'
    base_url = 'journal-calendar'

config = JournalCalendarConfig
