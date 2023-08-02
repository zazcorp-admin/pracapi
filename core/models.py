from django.db import models
from base.models import BaseModel

# Create your models here.


class Subscribed(BaseModel):
    email = models.EmailField()

    def __str__(self):
        return self.email