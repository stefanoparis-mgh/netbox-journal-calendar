import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import JournalIconConfig

class JournalIconConfigTable(NetBoxTable):
    content_type = tables.Column(
        linkify=True,
        verbose_name='Object Type'
    )
    # Cambiato in TemplateColumn per supportare il codice HTML/Template
    icon_class = tables.TemplateColumn(
        template_code='<i class="mdi {{ record.icon_class }}"></i> {{ record.icon_class }}',
        verbose_name='Icon Class'
    )
    id = tables.Column(linkify=True)

    actions = columns.ActionsColumn()

    class Meta(NetBoxTable.Meta):
        model = JournalIconConfig
        fields = ('pk', 'id', 'content_type', 'icon_class', 'actions')
        default_columns = ('content_type', 'icon_class', 'actions')