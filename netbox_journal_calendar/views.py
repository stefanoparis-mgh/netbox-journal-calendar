import calendar as py_calendar
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from extras.models import JournalEntry, Tag
from extras.choices import JournalEntryKindChoices
from dcim.models import Device
from virtualization.models import VirtualMachine
from ipam.models import Service
from .models import JournalIconConfig
from .forms import JournalIconConfigForm
from netbox.views import generic
from . import forms, models, tables
from .api import serializers
from netbox.api.viewsets import NetBoxModelViewSet
try:
    from netbox_map.models import ApplicationDeployment
except ImportError:
    ApplicationDeployment = None

User = get_user_model()



class JournalCalendarView(PermissionRequiredMixin, View):
    permission_required = 'extras.view_journalentry'

    def get(self, request):
        now = timezone.now()

        try:
            m = int(request.GET.get('month', now.month))
            y = int(request.GET.get('year', now.year))
        except (ValueError, TypeError):
            m, y = now.month, now.year
        icon_configs = {
            conf.content_type_id: conf.icon_class
            for conf in JournalIconConfig.objects.all()
        }
        DEFAULT_ICON = 'mdi mdi-tag-outline'

        kind_f = request.GET.get('kind', '')
        user_f = request.GET.get('user', '')
        device_f = request.GET.get('device', '')
        vm_f = request.GET.get('vm', '')
        service_f = request.GET.get('service', '')
        tag_f = request.GET.get('tag', '')
        application_f = request.GET.get('application')

        qs = JournalEntry.objects.filter(
            created__year=y, created__month=m
        ).select_related('created_by', 'assigned_object_type').prefetch_related('tags')

        if kind_f:
            qs = qs.filter(kind=kind_f)
        if user_f:
            qs = qs.filter(created_by_id=user_f)
        if tag_f:
            qs = qs.filter(tags__slug=tag_f)
        if application_f:
            app_ct = ContentType.objects.get(app_label='netbox_map', model='applicationdeployment')
            journal_entries = journal_entries.filter(
                assigned_object_type=app_ct,
                assigned_object_id=application_f
            )

        device_ct = ContentType.objects.get_for_model(Device)
        vm_ct = ContentType.objects.get_for_model(VirtualMachine)
        service_ct = ContentType.objects.get_for_model(Service)

        if device_f:
            qs = qs.filter(assigned_object_type=device_ct, assigned_object_id=device_f)
        if vm_f:
            qs = qs.filter(assigned_object_type=vm_ct, assigned_object_id=vm_f)
        if service_f:
            qs = qs.filter(assigned_object_type=service_ct, assigned_object_id=service_f)

        users = User.objects.filter(is_active=True).order_by('username')

        dev_ids = JournalEntry.objects.filter(assigned_object_type=device_ct).values_list('assigned_object_id',
                                                                                          flat=True).distinct()
        devices = Device.objects.filter(id__in=dev_ids).order_by('name')

        vm_ids = JournalEntry.objects.filter(assigned_object_type=vm_ct).values_list('assigned_object_id',
                                                                                     flat=True).distinct()
        vms = VirtualMachine.objects.filter(id__in=vm_ids).order_by('name')

        srv_ids = JournalEntry.objects.filter(assigned_object_type=service_ct).values_list('assigned_object_id',
                                                                                           flat=True).distinct()
        services = Service.objects.filter(id__in=srv_ids).order_by('name')

        applications = ApplicationDeployment.objects.all()

        tag_ids = JournalEntry.objects.values_list('tags', flat=True).distinct()
        tags = Tag.objects.filter(id__in=tag_ids).order_by('name')

        py_calendar.setfirstweekday(0)
        cal_matrix = py_calendar.monthcalendar(y, m)
        day_entries = {d: [] for d in range(0, 32)}
        for entry in qs:
            custom_icon = icon_configs.get(entry.assigned_object_type_id)
            if custom_icon:
                entry.obj_icon = custom_icon
            else:
                entry.obj_icon = DEFAULT_ICON
            day_entries[entry.created.day].append(entry)

        flat_days = []
        for week in cal_matrix:
            for d in week:
                flat_days.append({'num': d, 'list': day_entries.get(d, [])})

        query_params = request.GET.copy()

        prev_m = 12 if m == 1 else m - 1
        prev_y = y - 1 if m == 1 else y
        query_params['month'] = prev_m
        query_params['year'] = prev_year = prev_y
        prev_url = f"?{query_params.urlencode()}"

        next_m = 1 if m == 12 else m + 1
        next_y = y + 1 if m == 12 else y
        query_params['month'] = next_m
        query_params['year'] = next_y
        next_url = f"?{query_params.urlencode()}"

        context = {
            'days': flat_days,
            'month_name': py_calendar.month_name[m],
            'year': y,
            'prev_url': prev_url,
            'next_url': next_url,
            'today': now.day if (now.month == m and now.year == y) else 0,
            'kind_choices': list(JournalEntryKindChoices.CHOICES),
            'users': users,
            'devices': devices,
            'vms': vms,
            'services': services,
            'tags': tags,
            'current_kind': kind_f,
            'current_user': user_f,
            'current_device': device_f,
            'current_vm': vm_f,
            'current_service': service_f,
            'current_tag': tag_f,
            'applications': applications,
            'current_application': application_f,
        }
        return render(request, 'netbox_journal_calendar/calendar.html', context)


class JournalIconConfigEditView(generic.ObjectEditView):
    queryset = JournalIconConfig.objects.all()
    form = JournalIconConfigForm
    template_name = 'netbox_journal_calendar/journaliconconfig_edit.html'

class JournalIconConfigListView(generic.ObjectListView):
    queryset = models.JournalIconConfig.objects.all()
    table = tables.JournalIconConfigTable
    action_buttons = ("add",)


class JournalIconConfigDeleteView(generic.ObjectDeleteView):
    queryset = models.JournalIconConfig.objects.all()
    default_return_url = 'plugins:netbox_journal_calendar:journaliconconfig_list'

class JournalIconConfigChangeLogView(generic.ObjectChangeLogView):
    queryset = models.JournalIconConfig.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, model=self.queryset.model, *args, **kwargs)

class JournalIconConfigView(generic.ObjectView):
    queryset = models.JournalIconConfig.objects.all()

class JournalIconConfigViewSet(NetBoxModelViewSet):
    queryset = models.JournalIconConfig.objects.all()
    serializer_class = serializers.JournalIconConfigSerializer