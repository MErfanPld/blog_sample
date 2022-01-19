from django.db import models
from django.utils import timezone
from .db_base import BaseModel


class Cost(BaseModel):
    cost_date = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    cost_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح هزینه")
    cost_type = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="نوع هزینه")
    cost_amount = models.FloatField(
        blank=True, null=True, verbose_name="مبلغ هزینه")
    cost_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="توضیحات هزینه")
    
    def __str__(self):
        return self.cost_type

    class Meta:
        verbose_name = "مدیریت هزینه ها"
        verbose_name_plural = "  مدیریت هزینه ها"
        db_table = 'cost'

class Income(BaseModel):
    income_date = models.DateField(
        blank=True, null=True, verbose_name="تاریخ ")
    income_date = models.DateField(
        blank=True, null=True, verbose_name="تاریخ ")
    income_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح درامد")
    income_type = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="نوع درامد")
    income_amount = models.FloatField(
        blank=True, null=True, verbose_name="مبلغ درامد")
    income_description = models.TextField(
        blank=True, null=True, max_length=300, verbose_name="توضیحات درامد")
    
    class Meta:
        verbose_name = "مدیریت درآمدها"
        verbose_name_plural = "   مدیریت درآمدها"
        db_table = 'income'

class Debtor(BaseModel):
    debtor_received = models.FloatField(
        blank=True, null=True, verbose_name="دریافتی")
    debtor_to_borrow = models.FloatField(
        blank=True, null=True, verbose_name="قرض گرفتن")
    debtor_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح ")
    
    class Meta:
        verbose_name = "بدهکار"
        verbose_name_plural = "بدهکار"
        db_table = 'debtor'

class Creditor(BaseModel):
    creditor_payment = models.FloatField(
        blank=True, null=True, verbose_name="پرداختی")
    creditor_to_lend = models.FloatField(
        blank=True, null=True, verbose_name="قرض دادن")
    creditor_title = models.CharField(
        blank=True, null=True, max_length=30, verbose_name="شرح ")
    
    class Meta:
        verbose_name = "بستانکار"
        verbose_name_plural = " بستانکار"
        db_table = 'creditor'