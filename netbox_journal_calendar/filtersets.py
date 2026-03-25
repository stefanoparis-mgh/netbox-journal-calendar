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
        to_field_name='id',
        label='Device',
    )
    site = django_filters.ModelChoiceFilter(
        queryset=Site.objects.all(),
        method='filter_by_site',
        label='Sito'
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

        device_type = ContentType.objects.get_for_model(Device)

        # Otteniamo gli ID dei device come stringhe
        device_ids = Device.objects.filter(site=value).values_list('id', flat=True)
        device_ids_str = [str(id) for id in device_ids]  # Conversione in stringa

        return queryset.filter(
            assigned_object_type=device_type,
            assigned_object_id__in=device_ids_str
        )

    class Meta:
        model = JournalEntry
        fields = ['created', 'created_by', 'tag']
