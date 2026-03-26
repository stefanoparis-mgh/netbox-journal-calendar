from extras.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_journal_calendar:journalcalendar_list',
        link_text='Calendario Journal',
    ),
    PluginMenuItem(
        link='plugins:netbox_journal_calendar:journaliconconfig_list',
        link_text='Configurazione Icone',
        permissions=['netbox_journal_calendar.view_journaliconconfig']
    ),
)