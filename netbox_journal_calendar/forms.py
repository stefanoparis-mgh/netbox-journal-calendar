from django import forms
from django.contrib.auth import get_user_model
from extras.choices import JournalEntryKindChoices
from netbox.forms import NetBoxModelForm
from .models import JournalIconConfig
import json
import os
from django.contrib.contenttypes.models import ContentType


User = get_user_model()

class JournalCalendarFilterForm(forms.Form):

    kind = forms.ChoiceField(
        choices=[('', '---------')] + list(JournalEntryKindChoices.CHOICES),
        required=False,
        label='Kind'
    )

    created_by = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label='Created by'
    )

    q = forms.CharField(
        required=False,
        label='Find',
        widget=forms.TextInput(attrs={'placeholder': 'Find...'})
    )


class JournalIconConfigForm(NetBoxModelForm):
    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(
            app_label__in=['dcim', 'virtualization', 'ipam', 'tenancy', 'circuits', 'wireless', 'extras','netbox_custom_objects']
        ).order_by('app_label', 'model'),
        label='Object Type',
        widget=forms.Select(attrs={'class': 'netbox-static-select'}),
    )

    icon_class = forms.CharField(
        max_length=100,
        required=True,
        label='Icon Class',
        help_text='Icon name (es: mdi-calendar-check). '
                  'Full list on <a href="https://pictogrammers.com/library/mdi/" target="_blank">Material Design Icons</a>',
        widget=forms.TextInput(attrs={
            'placeholder': 'mdi-icon-name',
            'class': 'form-control'
        })
    )

    class Meta:
        model = JournalIconConfig
        fields = ('content_type', 'icon_class', 'tags')