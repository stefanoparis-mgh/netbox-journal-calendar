from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton
from django.utils.translation import gettext_lazy as _
from netbox.choices import ButtonColorChoices


calendar_item = PluginMenuItem(
    link='plugins:netbox_journal_calendar:journalcalendar_list',
    link_text=_('Journal Calendar'),
)

config_item = PluginMenuItem(
    link='plugins:netbox_journal_calendar:journaliconconfig_list',
    link_text=_('Icon Configuration'),
    buttons=(
        PluginMenuButton(
            link='plugins:netbox_journal_calendar:journaliconconfig_add',
            title=_('Add'),
            icon_class='mdi mdi-plus-thick',
            color=ButtonColorChoices.GREEN,
        ),
    )
)

menu = PluginMenu(
    label=_('Journal Calendar'),
    icon_class='mdi mdi-calendar-text',
    groups=(
        (_('View'), (calendar_item, config_item)),
    ),
)