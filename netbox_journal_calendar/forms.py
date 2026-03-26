from django import forms
from django.contrib.auth import get_user_model
from extras.choices import JournalEntryKindChoices
from netbox.forms import NetBoxModelForm
from .models import JournalIconConfig
import json
import os
from .utils import update_mdi_icons

User = get_user_model()

class JournalCalendarFilterForm(forms.Form):
    # Usiamo widget standard senza classi CSS particolari all'inizio
    kind = forms.ChoiceField(
        choices=[('', '---------')] + list(JournalEntryKindChoices.CHOICES),
        required=False,
        label='Tipo di nota'
    )

    created_by = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label='Creato da'
    )

    q = forms.CharField(
        required=False,
        label='Cerca',
        widget=forms.TextInput(attrs={'placeholder': 'Cerca...'})
    )


def get_icon_choices():
    file_path = os.path.join(os.path.dirname(__file__), 'mdi_icons.json')

    # Se il file non esiste, lo generiamo al volo
    if not os.path.exists(file_path):
        update_mdi_icons()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return [('mdi mdi-tag', 'Tag (Default)')]


class JournalIconConfigForm(forms.ModelForm):
    icon_class = forms.ChoiceField(
        choices=[],  # Popolato nel __init__
        label="Cerca Icona",
        help_text="Inizia a scrivere per cercare un'icona (es. 'server', 'wifi', 'cpu')",
        widget=forms.Select(attrs={'class': 'netbox-select2'})
    )

    class Meta:
        model = JournalIconConfig
        fields = ['content_type', 'icon_class']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Carichiamo le icone dinamicamente dal JSON
        self.fields['icon_class'].choices = get_icon_choices()