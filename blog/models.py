from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter


# my managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="ادرس")
    status = models.BooleanField(
        default=True, verbose_name="ایا نمایش داده شود؟")
    position = models.IntegerField(default=0, verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="ادرس")
    category = models.ManyToManyField(
        Category, verbose_name="دسته بندی", related_name="articles")
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to='images', verbose_name="تصویر")
    publish = models.DateTimeField(
        default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.all()])
    category_to_str.short_description = "دسته‌بندی"

    def category_published(self):
        return self.category.filter(status=True)

    objects = ArticleManager()
