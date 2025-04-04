# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    code = models.TextField(max_length=255, null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Request(models.Model):

    #__Request_FIELDS__
    reqdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    duedate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    postingflag = models.BooleanField()
    posteddate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    note = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)
    requesttype = models.TextField(max_length=255, null=True, blank=True)

    #__Request_FIELDS__END

    class Meta:
        verbose_name        = _("Request")
        verbose_name_plural = _("Request")


class Requestlines(models.Model):

    #__Requestlines_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    quantityexecuted = models.IntegerField(null=True, blank=True)
    warehousesource = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    warehousedestination = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)

    #__Requestlines_FIELDS__END

    class Meta:
        verbose_name        = _("Requestlines")
        verbose_name_plural = _("Requestlines")


class Warehouse(models.Model):

    #__Warehouse_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)
    type = models.TextField(max_length=255, null=True, blank=True)

    #__Warehouse_FIELDS__END

    class Meta:
        verbose_name        = _("Warehouse")
        verbose_name_plural = _("Warehouse")


class Entry(models.Model):

    #__Entry_FIELDS__
    entrydate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    postingflag = models.BooleanField()
    postingdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    entrytype = models.TextField(max_length=255, null=True, blank=True)
    note = models.TextField(max_length=255, null=True, blank=True)

    #__Entry_FIELDS__END

    class Meta:
        verbose_name        = _("Entry")
        verbose_name_plural = _("Entry")


class Entrylines(models.Model):

    #__Entrylines_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(null=True, blank=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    requestline = models.ForeignKey(RequestLines, on_delete=models.CASCADE)
    warehousesource = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    warehousedestintaion = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    #__Entrylines_FIELDS__END

    class Meta:
        verbose_name        = _("Entrylines")
        verbose_name_plural = _("Entrylines")



#__MODELS__END
