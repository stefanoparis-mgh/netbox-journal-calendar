from django.urls import path

from . import views

urlpatterns = [

    path('calendar/', views.JournalCalendarView.as_view(), name='journalcalendar_list'),

    path('icons/', views.JournalIconConfigListView.as_view(), name='journaliconconfig_list'),
    path('icons/add/', views.JournalIconConfigEditView.as_view(), name='journaliconconfig_add'),
    path('icons/<int:pk>/edit/', views.JournalIconConfigEditView.as_view(), name='journaliconconfig_edit'),
    path('icons/<int:pk>/', views.JournalIconConfigView.as_view(), name='journaliconconfig'),
    path('icons/<int:pk>/delete/', views.JournalIconConfigDeleteView.as_view(), name='journaliconconfig_delete'),
    path('icons/<int:pk>/changelog/', views.JournalIconConfigChangeLogView.as_view(), name='journaliconconfig_changelog'),
]