from django.urls import path
from .views import JournalCalendarView

urlpatterns = [
    path('', JournalCalendarView.as_view(), name='journal_calendar'),
]
