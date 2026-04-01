from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel

class JournalIconConfig(NetBoxModel):
    content_type = models.OneToOneField(
        to=ContentType,
        on_delete=models.CASCADE,
        related_name='journal_icon_config',
        verbose_name='Object Type',
        help_text='Type of the object (eg. Device, Virtual Machine) linked to the icon'
    )
    icon_class = models.CharField(
        max_length=100,
        verbose_name='Icon Class',
        help_text='MDI Class Name (eg. "mdi-router" o "mdi-server").'
    )

    class Meta:
        ordering = ['content_type']
        verbose_name = 'Journal Calendar icon configuration'
        verbose_name_plural = 'Journal Calendar icon configurations'

    def __str__(self):

        return f"{self.content_type} -> {self.icon_class}"

    def get_absolute_url(self):

        return reverse('plugins:netbox_journal_calendar:journaliconconfig', kwargs={'pk': self.pk})