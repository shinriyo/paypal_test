from django.db import models


class PurchaseHistory(models.Model):
    name = models.CharField(max_length=30)
    purchase_date = models.DateTimeField(auto_now_add=True)