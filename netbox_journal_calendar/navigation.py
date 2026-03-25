from netbox.plugins import PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_journal_calendar:journal_calendar',
        link_text='Calendario Journal',
        # Rimosso icon_class e icon per compatibilità NetBox 4.x
        permissions=['extras.view_journalentry'],
    ),
)
