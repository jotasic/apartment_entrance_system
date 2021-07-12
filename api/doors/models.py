from django.db import models

class DoorUseLog(models.Model): 
    door_number = models.CharField(max_length=4, unique=True)
    password    = models.CharField(max_length=4, unique=True)
    fee         = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'door_use_log'