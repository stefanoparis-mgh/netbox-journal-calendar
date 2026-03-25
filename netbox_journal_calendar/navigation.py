from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_journal_calendar:journal_calendar',
        link_text='Calendario Journal',
        icon='mdi mdi-calendar-month',
        permissions=['extras.view_journalentry'],
    ),
)
