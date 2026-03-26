from django.urls import path
from .views import JournalCalendarView

urlpatterns = [
    # La rotta principale del plugin
    path('', JournalCalendarView.as_view(), name='journal_calendar'),
]