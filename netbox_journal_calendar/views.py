import calendar
from datetime import date
from django.shortcuts import render
from django.views.generic import View
from extras.models import JournalEntry
from .filtersets import JournalCalendarFilterSet


class JournalCalendarView(View):
    def get(self, request):
        # Ottimizzazione query: caricamento anticipato di tag e utenti
        queryset = JournalEntry.objects.prefetch_related('tags', 'created_by').all()

        filterset = JournalCalendarFilterSet(request.GET, queryset=queryset)
        queryset = filterset.qs

        # Gestione data corrente e parametri URL
        today = date.today()
        year = int(request.GET.get('year', today.year))
        month = int(request.GET.get('month', today.month))

        # Logica navigazione mesi (gestione salto d'anno)
        if month == 1:
            prev_month, prev_year = 12, year - 1
        else:
            prev_month, prev_year = month - 1, year

        if month == 12:
            next_month, next_year = 1, year + 1
        else:
            next_month, next_year = month + 1, year

        # Recupero entries del mese filtrato
        entries = queryset.filter(created__year=year, created__month=month)

        calendar_data = {}
        for entry in entries:
            day = int(entry.created.day)
            if day not in calendar_data:
                calendar_data[day] = []
            calendar_data[day].append(entry)

        cal = calendar.Calendar(firstweekday=0)  # Lunedì come primo giorno
        month_days = cal.monthdayscalendar(year, month)

        context = {
            'year': year,
            'month': month,
            'month_name': calendar.month_name[month],
            'month_days': month_days,
            'calendar_data': calendar_data,
            'filter_form': filterset.form,
            'prev_month': prev_month,
            'prev_year': prev_year,
            'next_month': next_month,
            'next_year': next_year,
        }
        return render(request, 'netbox_journal_calendar/calendar.html', context)
