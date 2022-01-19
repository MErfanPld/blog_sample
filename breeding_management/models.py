from django.db import models
from basic_information.models import HallInformation , Vaccin
from .db_base import BaseModel
from django.utils.translation import gettext_lazy as _


class DrugRegistration(BaseModel):
    class Meta:
        verbose_name = "ثبت دارو  "
        verbose_name_plural = "ثبت دارو "
        db_table = 'drugregistration'
    # ? فیلدهای دارو
    date  = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    medicine_name = models.CharField(max_length=100, verbose_name="نام دارو")
    consumption_seam = models.CharField(max_length=255, verbose_name="دز مصرف")
    description_of_drug_use = models.TextField(
        blank=True, null=True, verbose_name="توضیحات مصرف دارو")
    drug_performance_report = models.TextField(
        blank=True, null=True, verbose_name="گزارش عملکرد دارو")


class VaccineRegistration(BaseModel):
    class Meta:
        verbose_name = "ثبت واکسن"
        verbose_name_plural = "ثبت واکسن"
        db_table = 'vaccinregistration'
    # ? فیلدهای واکسن
    date  = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    vaccin_name = models.ManyToManyField(
        Vaccin,
        verbose_name=_('واکسن '),
        blank=True,
        
        related_name="vaccinname",
        related_query_name="vaccinname",
    )    
    vaccine_report = models.TextField(
        blank=True, null=True, verbose_name="گزارش مصرف واکسن")


class ExperimentRegistration(BaseModel):
    class Meta:
        verbose_name = "ثبت آزمایش"
        verbose_name_plural = "ثبت آزمایش "
        db_table = 'experimentregistration'
    # ? فیلدهای آزمایش
    date  = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    test_name = models.CharField(max_length=100, verbose_name="نام آزمایش")
    number_of_samples = models.IntegerField(verbose_name="تعداد نمونه")
    upload_test_results = models.ImageField(upload_to='Trial/', verbose_name="اپلود نتیجه ازمایش")

    
class Weightlifting (BaseModel) :
    date  = models.DateField(blank=True, null=True, verbose_name="تاریخ ")
    hall = models.ForeignKey(HallInformation, null=True, on_delete=models.SET_NULL,
            related_name="halls", verbose_name="سالن")
    age = models.FloatField ( blank=False , verbose_name="سن " )
    weight_average = models.FloatField( blank=False , verbose_name='میانگین وزن')
    class Meta:
        verbose_name = "وزن کشی "
        verbose_name_plural = "وزن کشی  "
        db_table = 'weightlifting'

class Daily_Informations(BaseModel):
    date  = models.DateField(verbose_name="تاریخ " )
    hall = models.ForeignKey(HallInformation, null=True, on_delete=models.SET_NULL,
            related_name="hall", verbose_name="سالن")
    losses = models.IntegerField(verbose_name='تلفات جوجه', default=0,null=True, blank=True)
    knockout = models.IntegerField(verbose_name='حذفیات جوجه', default=0,null=True, blank=True)
    temprature_max = models.FloatField(verbose_name='کمترین دمای روز', null=True, blank=True)
    temprature_min = models.FloatField(verbose_name='بیشترین دمای روز', null=True, blank=True)
    seed = models.FloatField(verbose_name='دان مصرفی در روز', null=True, blank=True)
    water = models.FloatField(verbose_name='آب مصرفی' , default=0,null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True, default=' ثبت نشده', max_length=200 ,verbose_name='توضیحات')

    class Meta:
        verbose_name = "ثبت اطلاعات روزانه"
        verbose_name_plural = "ثبت اطلاعات روزانه"
        db_table = 'dailyinformation'
        indexes = [
            models.Index(fields=['date', ]),
        ]

    def Total_Losses (self) :
        total_loses = 0
        for item in Daily_Informations.objects.all() :
            if item.is_active == True :
                try :
                    total_loses += float(item.losses)
                except :
                    print('there is no losage')
        return total_loses    
    
    def Total_Seed(self) :
        total_seed = 0
        for item in Daily_Informations.objects.all() :
            if item.is_active == True :
                try:
                    total_seed += float(item.seed)
                except :
                    print('there is no seed for today')
        return total_seed