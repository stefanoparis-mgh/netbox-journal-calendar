import calendar as py_calendar
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

# Import dei modelli NetBox
from extras.models import JournalEntry
from extras.choices import JournalEntryKindChoices
from dcim.models import Device
from virtualization.models import VirtualMachine
from ipam.models import Service

User = get_user_model()


class JournalCalendarView(PermissionRequiredMixin, View):
    permission_required = 'extras.view_journalentry'

    def get(self, request):
        now = timezone.now()

        # 1. Recupero parametri Mese/Anno
        try:
            m = int(request.GET.get('month', now.month))
            y = int(request.GET.get('year', now.year))
        except (ValueError, TypeError):
            m, y = now.month, now.year

        # 2. DEFINIZIONE VARIABILI PER I FILTRI (Sempre eseguita)
        # Identifichiamo i ContentType per filtrare i menu a tendina
        device_ct = ContentType.objects.get_for_model(Device)
        vm_ct = ContentType.objects.get_for_model(VirtualMachine)
        service_ct = ContentType.objects.get_for_model(Service)

        # Utenti: tutti quelli attivi
        users = User.objects.filter(is_active=True).order_by('username')

        # Filtriamo le liste per mostrare solo chi ha log (Evita liste infinite)
        dev_ids = JournalEntry.objects.filter(assigned_object_type=device_ct).values_list('assigned_object_id',
                                                                                          flat=True).distinct()
        devices = Device.objects.filter(id__in=dev_ids).order_by('name')

        vm_ids = JournalEntry.objects.filter(assigned_object_type=vm_ct).values_list('assigned_object_id',
                                                                                     flat=True).distinct()
        vms = VirtualMachine.objects.filter(id__in=vm_ids).order_by('name')

        srv_ids = JournalEntry.objects.filter(assigned_object_type=service_ct).values_list('assigned_object_id',
                                                                                           flat=True).distinct()
        services = Service.objects.filter(id__in=srv_ids).order_by('name')

        # 3. RECUPERO PARAMETRI GET
        kind_f = request.GET.get('kind', '')
        user_f = request.GET.get('user', '')
        device_f = request.GET.get('device', '')
        vm_f = request.GET.get('vm', '')
        service_f = request.GET.get('service', '')

        # 4. QUERYSET FILTRATA PER IL CALENDARIO
        qs = JournalEntry.objects.filter(
            created__year=y, created__month=m
        ).select_related('created_by', 'assigned_object_type')

        if kind_f:
            qs = qs.filter(kind=kind_f)
        if user_f:
            qs = qs.filter(created_by_id=user_f)
        if device_f:
            qs = qs.filter(assigned_object_type=device_ct, assigned_object_id=device_f)
        if vm_f:
            qs = qs.filter(assigned_object_type=vm_ct, assigned_object_id=vm_f)
        if service_f:
            qs = qs.filter(assigned_object_type=service_ct, assigned_object_id=service_f)

        # 5. COSTRUZIONE MATRICE CALENDARIO
        py_calendar.setfirstweekday(0)
        cal_matrix = py_calendar.monthcalendar(y, m)
        day_entries = {d: [] for d in range(0, 32)}

        for entry in qs:
            day_entries[entry.created.day].append(entry)

        flat_days = []
        for week in cal_matrix:
            for d in week:
                flat_days.append({
                    'num': d,
                    'list': day_entries.get(d, []) if d > 0 else []
                })

        # 6. CONTESTO PER IL TEMPLATE
        context = {
            'days': flat_days,
            'month_name': py_calendar.month_name[m],
            'year': y,
            'prev_url': f"?month={12 if m == 1 else m - 1}&year={y - 1 if m == 1 else y}",
            'next_url': f"?month={1 if m == 12 else m + 1}&year={y + 1 if m == 12 else y}",
            'today': now.day if (now.month == m and now.year == y) else 0,
            'kind_choices': list(JournalEntryKindChoices.CHOICES),
            'users': users,
            'devices': devices,
            'vms': vms,
            'services': services,
            'current_kind': kind_f,
            'current_user': user_f,
            'current_device': device_f,
            'current_vm': vm_f,
            'current_service': service_f,
        }
        return render(request, 'netbox_journal_calendar/calendar.html', context)