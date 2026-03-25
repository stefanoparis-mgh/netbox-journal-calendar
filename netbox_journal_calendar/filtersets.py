import django_filters
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from extras.models import JournalEntry, Tag
from dcim.models import Device, Site
from virtualization.models import VirtualMachine
from ipam.models import Service


class JournalCalendarFilterSet(django_filters.FilterSet):
    device = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        field_name='assigned_object_id',
        to_field_name='id',
        label='Device',
    )
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        field_name='assigned_object_id',
        to_field_name='id',
        label='Virtual Machine',
    )
    service = django_filters.ModelMultipleChoiceFilter(
        queryset=Service.objects.all(),
        field_name='assigned_object_id',
        to_field_name='id',
        label='Service',
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

        # Otteniamo i ContentType necessari
        device_ct = ContentType.objects.get_for_model(Device)
        vm_ct = ContentType.objects.get_for_model(VirtualMachine)
        service_ct = ContentType.objects.get_for_model(Service)

        # IDs degli oggetti nel sito selezionato
        device_ids = list(Device.objects.filter(site=value).values_list('id', flat=True))
        vm_ids = list(VirtualMachine.objects.filter(site=value).values_list('id', flat=True))

        # Per i servizi, cerchiamo quelli collegati a device o VM di quel sito
        service_ids = list(Service.objects.filter(
            Q(device__site=value) | Q(virtual_machine__site=value)
        ).values_list('id', flat=True))

        # Convertiamo tutto in stringhe per il match con assigned_object_id
        device_ids_str = [str(x) for x in device_ids]
        vm_ids_str = [str(x) for x in vm_ids]
        service_ids_str = [str(x) for x in service_ids]

        # Filtriamo il queryset originale combinando le condizioni
        return queryset.filter(
            (Q(assigned_object_type=device_ct) & Q(assigned_object_id__in=device_ids_str)) |
            (Q(assigned_object_type=vm_ct) & Q(assigned_object_id__in=vm_ids_str)) |
            (Q(assigned_object_type=service_ct) & Q(assigned_object_id__in=service_ids_str))
        )

    class Meta:
        model = JournalEntry
        fields = ['created_by', 'tag']
