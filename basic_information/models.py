from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.expressions import F, ValueRange
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .db_base import BaseModel

# Create your models here.


class OwnerInformation(BaseModel):
    first_name = models.CharField(max_length=150, verbose_name="نام")
    last_name = models.CharField(max_length=200, verbose_name="نام خانوادگی")
    mobile_number = models.CharField(
        max_length=11, verbose_name="شماره همراه")
    number_of_farms = models.IntegerField(
        blank=True, null=True, verbose_name="تعداد فارم")
    total_capacity = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="ظرفیت کل")
    description = models.TextField(
        blank=True, null=True, verbose_name="توضیحات")
    
    

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "اطلاعات مالک"
        verbose_name_plural = "   اطلاعات مالک"
        db_table = 'ownerinformaions'


class FarmInformation(BaseModel):
    farm_name = models.CharField(max_length=100,  verbose_name="نام فارم")
    number_of_halls = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="تعداد سالن")
    farm_capacity = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="ظرفیت فارم ")
    description = models.TextField(
        blank=True, null=True, verbose_name="توضیحات")

    def __str__(self):
        return self.farm_name

    class Meta:
        verbose_name = "اطلاعات فارم"
        verbose_name_plural = "  اطلاعات فارم"
        db_table = 'farminformation'

class StoreRoom (BaseModel) :
    capacity = models.FloatField(verbose_name='ظرفیت' , null=True , blank = True)
    assigned_farm = models.ForeignKey(FarmInformation,null = True, on_delete=models.SET_NULL,
            related_name="store_room_farm", verbose_name="فارم")
    description = models.TextField(
        blank=True, null=True, verbose_name="توضیحات")

class HallInformation(BaseModel):
    assigned_farm = models.ForeignKey(FarmInformation, on_delete=models.SET_NULL,
            null  = True, related_name="hall_farms", verbose_name="فارم")
    hall_number = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="شماره سالن")
    capacity = models.IntegerField(
        blank=True, null=True, default="0", verbose_name="ظرفیت")
    description = models.TextField(
        blank=True, null=True, verbose_name="توضیحات")

    class Meta:
        verbose_name = "اطلاعات سالن"
        verbose_name_plural = " اطلاعات سالن"
        db_table = 'hallinformaions'


class StandardInformation(BaseModel):
    # number_of_days = models. (شماره روز)
     
    chicken_type = models.CharField(
        blank=False , null=False , max_length=30,default='مشخص نشده', verbose_name='نژاد جوجه')

    food_constant = models.FloatField(
        blank=True, null=True, default="1", verbose_name=" ضریب تبدیل غذایی ")
    
    collective_seeds = models.FloatField(
        blank=True, null=True, default="0", verbose_name="مصرف تجمعی خوراک")
    
    daily_consumption = models.FloatField(
        blank=True, null=True, default="0", verbose_name="مصرف روزانه خوراک ")
    
    weight = models.FloatField(
        blank=True, null=True, default="0", verbose_name="وزن")
   
    daily_weight_gain = models.FloatField(
        blank=True, null=True, default="0", verbose_name="افزایش وزن روزانه")
    
    class Meta:
        verbose_name = "اطلاعات استاندارد"
        verbose_name_plural = "اطلاعات استاندارد"
        db_table = 'standardinformaions'


class DurationInformation(BaseModel):
    class Meta:
        verbose_name = "اطلاعات دوره "
        verbose_name_plural = "اطلاعات دوره"
        db_table = 'durationinformaions'

    duration_number = models.FloatField(blank=False , verbose_name='شماره دوره', null=True)
    duration_season = models.CharField(blank=False , null=True, verbose_name='فصل دوره' , max_length=30)
    start_date = models.DateField(blank=True ,null=True , verbose_name='تاریخ شروع دوره ' )
    finish_date = models.DateField(blank=True ,null=True , verbose_name='تاریخ اتمام دوره' )
    duration_duration = models.FloatField(blank=True , verbose_name='طول مدت دوره', null=True)
    chicken_number = models.IntegerField(blank=True , verbose_name='تعداد جوجه' , null=True)

class Vaccin (BaseModel) :
    name = CharField(verbose_name='نام واکسن' , max_length=50)
    type = CharField(verbose_name='نوع واکسن' , max_length=50 , null=True , blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "vaccin"


class ChickenInformation(BaseModel):
    class Meta:
        verbose_name = "اطلاعات جوجه "
        verbose_name_plural = "اطلاعات جوجه"
        db_table = 'chickeninformaions'

    chicken_breed = models.CharField(blank=False , verbose_name='نژاد جوجه ', max_length=30 , default='نژاد')
    breeding_flock_name = models.CharField(blank=False , verbose_name='نام گله مادر ' , max_length=30 , default='نام')
    breeding_flock_age = models.FloatField(blank = False , verbose_name='سن گله مادر' ,default=0) 
    first_weight = models.FloatField(blank = False , verbose_name='وزن ورود'  , default=0)
    vaccin = models.ManyToManyField(
        Vaccin,
        verbose_name=_('واکسن مادری'),
        blank=True,
        
        related_name="flockvaccin",
        related_query_name="flockvaccin",
    )

class BlackoutProgram(BaseModel):
    from_weight = models.FloatField(blank=True ,null=True, verbose_name='از وزن')
    to_weight = models.FloatField(blank=True ,null=True, verbose_name='تا وزن')
    from_age = models.FloatField(blank=True ,null=True, verbose_name='از سن')
    to_age = models.FloatField(blank=True ,null=True, verbose_name='تا سن')
    blackout_hours = models.FloatField(blank=False , verbose_name='تعداد ساعت خاموشی' , default=0)
    blackout_type = models.CharField(blank=False , verbose_name='نوع خاموشی' , max_length=20 , default=0)
    start_time = models.CharField(blank=False , verbose_name='ساعت شروع خاموشی' , max_length=6)
    finish_time = models.CharField(blank=False , verbose_name='ساعت پایان خاموشی' , max_length=6)

    class Meta:
        verbose_name = "برنامه خاموشی"
        verbose_name_plural = "برنامه خاموشی"
        db_table = 'blackoutprogram'



class DietPlan(BaseModel):
    from_weight = models.FloatField(blank=True ,null=True ,verbose_name='از وزن')
    to_weight = models.FloatField(blank=True ,null=True ,verbose_name='تا وزن')
    from_age = models.FloatField(blank=True ,null=True ,verbose_name='از سن')
    to_age = models.FloatField(blank=True ,null=True ,verbose_name='تا سن')
    diet_type = models.CharField(max_length=20 , verbose_name='نوع جیره غذایی', blank=True)
    #diet_formula = models.

    class Meta:
        verbose_name = "برنامه جیره غذایی"
        verbose_name_plural = "برنامه جیره غذایی"
        db_table = 'dietplan'


class VaccineProgramInformation(BaseModel):
    age = models.FloatField(blank=False , verbose_name=' سن' , default=0)
    vaccin = models.ManyToManyField(
        Vaccin,
        verbose_name=_('واکسن '),
        blank=True,
        
        related_name="vaccin",
        related_query_name="vaccin",
    )    
    usage = models.CharField(max_length=30 , verbose_name='نوع مصرف' , default='نوع')
    class Meta:
        verbose_name = "اطلاعات واکسن "
        verbose_name_plural = "اطلاعات واکسن"
        db_table = "vaccin_programm"

