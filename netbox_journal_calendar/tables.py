import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import JournalIconConfig

class JournalIconConfigTable(NetBoxTable):
    content_type = tables.Column(
        linkify=True,
        verbose_name='Object Type'
    )
    icon_class = tables.Column(
        verbose_name='Icon Class'
    )
    id = tables.Column(linkify=True)

    actions = columns.ActionsColumn()

    class Meta(NetBoxTable.Meta):
        model = JournalIconConfig
        fields = ('pk', 'id', 'content_type', 'icon_class', 'actions')
        default_columns = ('content_type', 'icon_class', 'actions')