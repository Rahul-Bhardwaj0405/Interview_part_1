from pickle import TRUE
from django.db import models

# Create your models here.

class UploadedTranasaction(models.Model):
    bank_name = models.CharField(max_length=50)
    transaction_type = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    TXN_DATE = models.DateField(max_length=50, null=True, blank=True)
    IRCTC_ORDER_NO = models.CharField(max_length=50, null=True, blank=True)
    BANK_BOOKING_REF_NO = models.CharField(max_length=50, null=True, blank=True)
    BOOKING_AMOUNT = models.IntegerField(null=True, blank=True)
    CREDITED_ON = models.DateField(max_length=50, null=True, blank=True)
