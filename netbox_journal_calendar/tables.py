import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from django.utils.safestring import mark_safe
from .models import JournalIconConfig

class JournalIconConfigTable(NetBoxTable):
    content_type = tables.Column(
        linkify=True,
        verbose_name="Tipo di Oggetto"
    )
    # Colonna personalizzata per mostrare l'icona visivamente
    icon_class = tables.Column(
        verbose_name="Icona Configurata"
    )

    class Meta(NetBoxTable.Meta):
        model = JournalIconConfig
        fields = ('pk', 'id', 'content_type', 'icon_class', 'actions')
        default_columns = ('content_type', 'icon_class')

    # Trasforma il testo in HTML per mostrare l'icona
    def render_icon_class(self, value):
        return mark_safe(
            f'<i class="{value}" style="font-size: 1.4rem; vertical-align: middle; margin-right: 10px;"></i>'
            f'<code class="text-muted">{value}</code>'
        )