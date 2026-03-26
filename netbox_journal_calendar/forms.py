from django import forms
from django.contrib.auth import get_user_model
from extras.choices import JournalEntryKindChoices

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