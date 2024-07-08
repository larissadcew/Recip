from django.db import models
from django.contrib.auth.models import User

class Receipt(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	name = models.CharField(max_length=100, default='something')
	price = models.IntegerField(default=0)
	quantity = models.IntegerField(default =0)
	total = models.IntegerField(default=0)
