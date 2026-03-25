import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from extras.models import JournalEntry, Tag
from dcim.models import Device, Site
from extras.choices import JournalEntryKindChoices

class JournalCalendarFilterSet(NetBoxModelFilterSet):
    device = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        field_name='assigned_object_id',
        label='Device',
    )
    site = django_filters.ModelChoiceFilter(
        queryset=Site.objects.all(),
        method='filter_by_site',
        label='Sito'
    )
    kind = django_filters.MultipleChoiceFilter(
        choices=JournalEntryKindChoices,
        label='Tipo',
        widget=django_filters.widgets.CSVWidget
    )
    tag = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        field_name='tags__slug',
        to_field_name='slug',
        label='Tags',
    )

    def filter_by_site(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(device__site=value)

    class Meta:
        model = JournalEntry
        fields = ['id', 'created', 'created_by', 'kind', 'cf', 'tag']
