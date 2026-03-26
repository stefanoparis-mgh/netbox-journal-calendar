from django.db import models
from django.contrib.contenttypes.models import ContentType

class JournalIconConfig(models.Model):
    content_type = models.OneToOneField(
        to=ContentType,
        on_delete=models.CASCADE,
        related_name='journal_icon_config'
    )
    # Rimosso choices: la logica di selezione si sposta nel Form
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.content_type}"