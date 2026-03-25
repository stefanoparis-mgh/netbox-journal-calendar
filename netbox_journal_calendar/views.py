import calendar
from datetime import date
from django.shortcuts import render
from django.views.generic import View
from extras.models import JournalEntry
from .filtersets import JournalCalendarFilterSet


class JournalCalendarView(View):
    def get(self, request):
        queryset = JournalEntry.objects.prefetch_related('tags', 'created_by').all()
        filterset = JournalCalendarFilterSet(request.GET, queryset=queryset)
        queryset = filterset.qs

        today = date.today()
        # Fallback sicuro se i parametri mancano o sono errati
        try:
            year = int(request.GET.get('year', today.year))
            month = int(request.GET.get('month', today.month))
            if not (1 <= month <= 12): month = today.month
        except ValueError:
            year, month = today.year, today.month

        # Navigazione
        prev_month, prev_year = (12, year - 1) if month == 1 else (month - 1, year)
        next_month, next_year = (1, year + 1) if month == 12 else (month + 1, year)

        entries = queryset.filter(created__year=year, created__month=month)

        calendar_data = {}
        for entry in entries:
            day = int(entry.created.day)
            if day not in calendar_data:
                calendar_data[day] = []
            calendar_data[day].append(entry)

        # FORZA LA LISTA: Fondamentale per il template
        cal = calendar.Calendar(firstweekday=0)
        month_days = list(cal.monthdayscalendar(year, month))

        context = {
            'year': year,
            'month': month,
            'month_name': calendar.month_name[month],
            'month_days': month_days,  # Questa deve essere una lista di liste
            'calendar_data': calendar_data,
            'filter_form': filterset.form,
            'prev_month': prev_month, 'prev_year': prev_year,
            'next_month': next_month, 'next_year': next_year,
        }
        return render(request, 'netbox_journal_calendar/calendar.html', context)
