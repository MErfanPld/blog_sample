from django.db import models

class BaseModel(models.Model) :
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)
    date_deactivated = models.DateField(verbose_name='تاریخ پاک شدن این رکورد', null=True )
    date_edited = models.DateField(verbose_name='تاریخ ادیت شدن این رکورد', null=True)
    id_base_record = models.IntegerField(verbose_name='آیدی رکورد اصلی ', null=True)
    # این ستون از جدول میگه ک این رکورد در واقع ادیت شده ی کدوم رکورد هست ....اگر یک رکورد چندبار ادیت بشه قاعدتا 
    # هربار ایدی همان اولین رکورد ثبت شده در این سطر وارد میشود ن آیدی رکورد قبل از این ادیت
    #basemodel_ptr = models.CharField(max_length=10 , default='who R U' , null=True)