from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_weight = models.IntegerField()
    product_height = models.IntegerField()
    product_color = models.CharField(max_length=255)
    product_preview = models.ImageField(upload_to='uploads/photo/')

    def __unicode__(self):
        return self.product_name
