from netbox.plugins import PluginMenu, PluginMenuItem

item1 = PluginMenuItem(
    link='plugins:netbox_journal_calendar:journal_calendar',
    link_text='Calendario Journal'
)

menu = PluginMenu(
    label='Journal Calendar',
    groups=(
        ('Visualizzazione', (item1,)),
    ),
    icon_class='mdi mdi-calendar-month'
)
