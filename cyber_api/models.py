from django.db import models


class Person(models.Model):
    full_name = models.CharField(verbose_name = 'tulliq ismi', max_length=65, blank=True, null=False)
    phone_number = models.CharField(verbose_name = 'tellfon raqam', max_length=20, blank=True, null=True)
    telegram_id = models.CharField(max_length=8)
    district = models.CharField(verbose_name = 'tuman', max_length = 20)
    level = models.IntegerField(verbose_name = 'daraja', default=0)

    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    
    class Meta:
        def __str__(self):
            return self.full_name

