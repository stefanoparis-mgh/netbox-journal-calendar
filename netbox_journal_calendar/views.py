import calendar
from datetime import datetime
from django.shortcuts import render
from django.views.generic import View
from extras.models import JournalEntry
from .filtersets import JournalCalendarFilterSet


class JournalCalendarView(View):
    def get(self, request):
        queryset = JournalEntry.objects.all()
        filterset = JournalCalendarFilterSet(request.GET, queryset=queryset)
        queryset = filterset.qs

        today = datetime.now()
        year = int(request.GET.get('year', today.year))
        month = int(request.GET.get('month', today.month))

        entries = queryset.filter(created__year=year, created__month=month)

        calendar_data = {}
        for entry in entries:
            day = entry.created.day
            if day not in calendar_data:
                calendar_data[day] = []
            calendar_data[day].append(entry)

        cal = calendar.Calendar(firstweekday=0)
        month_days = cal.monthdayscalendar(year, month)

        context = {
            'year': year,
            'month': month,
            'month_name': calendar.month_name[month],
            'month_days': month_days,
            'calendar_data': calendar_data,
            'filter_form': filterset.form,
        }
        return render(request, 'netbox_journal_calendar/calendar.html', context)
