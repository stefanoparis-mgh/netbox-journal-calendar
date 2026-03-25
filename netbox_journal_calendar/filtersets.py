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
        method='filter_by_device',
        label='Device',
    )
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        method='filter_by_vm',
        label='Virtual Machine',
    )
    service = django_filters.ModelMultipleChoiceFilter(
        queryset=Service.objects.all(),
        method='filter_by_service',
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

    # Filtro specifico per Device
    def filter_by_device(self, queryset, name, value):
        if not value: return queryset
        ct = ContentType.objects.get_for_model(Device)
        ids = [str(obj.id) for obj in value]
        return queryset.filter(assigned_object_type=ct, assigned_object_id__in=ids)

    # Filtro specifico per VM
    def filter_by_vm(self, queryset, name, value):
        if not value: return queryset
        ct = ContentType.objects.get_for_model(VirtualMachine)
        ids = [str(obj.id) for obj in value]
        return queryset.filter(assigned_object_type=ct, assigned_object_id__in=ids)

    # Filtro specifico per Service
    def filter_by_service(self, queryset, name, value):
        if not value: return queryset
        ct = ContentType.objects.get_for_model(Service)
        ids = [str(obj.id) for obj in value]
        return queryset.filter(assigned_object_type=ct, assigned_object_id__in=ids)

    # Filtro globale per Sito (Device + VM + Service nel sito)
    def filter_by_site(self, queryset, name, value):
        if not value: return queryset

        device_ct = ContentType.objects.get_for_model(Device)
        vm_ct = ContentType.objects.get_for_model(VirtualMachine)
        service_ct = ContentType.objects.get_for_model(Service)

        # Raccogliamo gli ID degli oggetti nel sito
        d_ids = [str(id) for id in Device.objects.filter(site=value).values_list('id', flat=True)]
        v_ids = [str(id) for id in VirtualMachine.objects.filter(site=value).values_list('id', flat=True)]
        s_ids = [str(id) for id in Service.objects.filter(Q(device__site=value) | Q(virtual_machine__site=value)).values_list('id', flat=True)]

        return queryset.filter(
            (Q(assigned_object_type=device_ct) & Q(assigned_object_id__in=d_ids)) |
            (Q(assigned_object_type=vm_ct) & Q(assigned_object_id__in=v_ids)) |
            (Q(assigned_object_type=service_ct) & Q(assigned_object_id__in=s_ids))
        )

    class Meta:
        model = JournalEntry
        fields = ['created_by', 'tag']
