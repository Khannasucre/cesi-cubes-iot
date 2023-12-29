from django.db import models

class Meteo(models.Model):
    id = models.AutoField(primary_key=True)
    temperature = models.fields.FloatField()
    humidity = models.fields.FloatField()
    pressure = models.fields.FloatField()
