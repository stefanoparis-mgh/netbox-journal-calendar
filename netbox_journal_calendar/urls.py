from django.urls import path

from . import views

urlpatterns = [
    # La rotta principale del plugin
    path('', JournalCalendarView.as_view(), name='journal_calendar'),
    path('calendar/', views.JournalCalendarView.as_view(), name='journalcalendar_list'),
    # Gestione Icone
    path('icons/', views.JournalIconConfigListView.as_view(), name='journaliconconfig_list'),
    path('icons/add/', views.JournalIconConfigEditView.as_view(), name='journaliconconfig_add'),
    path('icons/<int:pk>/edit/', views.JournalIconConfigEditView.as_view(), name='journaliconconfig_edit'),
    path('icons/<int:pk>/delete/', views.JournalIconConfigDeleteView.as_view(), name='journaliconconfig_delete'),
]