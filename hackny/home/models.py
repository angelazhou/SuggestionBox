from django.db import models
from django_extensions.db.models import TimeStampedModel

class suggestion(TimeStampedModel):
	data = models.CharField(max_length=10000)
