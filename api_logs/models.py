from django.db import models
from api_core.models import Agent


class Event(models.Model):
    LEVEL_CHOICES = (
        ("1", "CRITICAL"),
        ("2", "DEBUG"),
        ("3", "ERROR"),
        ("4", "WARNING"),
        ("5", "INFO"),
    )
    level = models.CharField("Level", max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField("Informações")
    shelved = models.BooleanField("Arquivado", default=False)
    date = models.DateTimeField("Data", auto_now=True)
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)
