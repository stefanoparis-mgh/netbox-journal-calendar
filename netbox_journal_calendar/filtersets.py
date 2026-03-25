import django_filters
from extras.models import JournalEntry, Tag
from dcim.models import Device, Site
from extras.choices import JournalEntryKindChoices
from django.contrib.contenttypes.models import ContentType

# Usiamo django_filters.FilterSet per avere il controllo totale sui campi
class JournalCalendarFilterSet(django_filters.FilterSet):
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

        # 1. Otteniamo il ContentType per il modello Device
        device_type = ContentType.objects.get_for_model(Device)

        # 2. Filtriamo le JournalEntry che:
        #    - Sono collegate a un Device (assigned_object_type)
        #    - Il cui ID (assigned_object_id) appartiene a un Device di quel Sito
        device_ids = Device.objects.filter(site=value).values_list('id', flat=True)

        return queryset.filter(
            assigned_object_type=device_type,
            assigned_object_id__in=device_ids
        )

    class Meta:
        model = JournalEntry
        fields = ['id', 'created', 'created_by', 'kind', 'tag']
