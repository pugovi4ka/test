from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_weight = models.IntegerField()
    product_height = models.IntegerField()
    product_color = models.CharField(max_length=255)
    product_color_once_more = models.CharField(max_length=255)
    product_preview = models.ImageField(upload_to='uploads/photo/')

    def __unicode__(self):
        return self.product_name


class Statistic(models.Model):
    url = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    response_status_code = models.CharField(max_length=255)
