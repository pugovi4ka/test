# coding=utf-8
from django.core.mail import mail_admins
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from mycatalog.models import Product

def sent_mail(sender, instance, **kwargs):
    mail_admins(u'Product has been changed', u'Product %s has been changed' % instance.product_name)

pre_save.connect(sent_mail, sender=Product)
pre_delete.connect(sent_mail, sender=Product)

