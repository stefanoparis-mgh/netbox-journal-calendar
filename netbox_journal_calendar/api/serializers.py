from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import JournalIconConfig

class JournalIconConfigSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_journal_calendar-api:journaliconconfig-detail'
    )

    class Meta:
        model = JournalIconConfig
        fields = (
            'id', 'url', 'display', 'icon_class', 'content_type',
            'tags', 'custom_fields', 'created', 'last_updated',
        )