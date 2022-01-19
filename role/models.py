from django.db import models


# Create your models here.


class RolesModel(models.Model):
    role_name = models.CharField(max_length=100, verbose_name="نام نقش")
    role_permission = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "نقش"
        verbose_name_plural = "نقش ها"

    def __str__(self):
        return self.role_name
