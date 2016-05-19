# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Class(models.Model):
    classyear = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    coordinator = models.ForeignKey('Donor', models.DO_NOTHING, db_column='coordinator', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class Donation(models.Model):
    donationno = models.DecimalField(primary_key=True, max_digits=12, decimal_places=0)
    donorid = models.ForeignKey('Donor', models.DO_NOTHING, db_column='donorid', blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    paymethod = models.CharField(max_length=-1, blank=True, null=True)
    installments = models.IntegerField(blank=True, null=True)
    pledge_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donation'


class Donor(models.Model):
    donorid = models.DecimalField(primary_key=True, max_digits=9, decimal_places=0)
    fname = models.CharField(max_length=30, blank=True, null=True)
    mname = models.CharField(max_length=30, blank=True, null=True)
    lname = models.CharField(max_length=30, blank=True, null=True)
    contactno = models.CharField(max_length=12, blank=True, null=True)
    creditno = models.DecimalField(max_digits=16, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    donor_affiliation = models.ForeignKey('self', models.DO_NOTHING, db_column='donor_affiliation', blank=True, null=True)
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    category = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donor'


class EventDonation(models.Model):
    eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='eventid')
    donorid = models.ForeignKey(Donor, models.DO_NOTHING, db_column='donorid')
    donationno = models.ForeignKey(Donation, models.DO_NOTHING, db_column='donationno')
    id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'event_donation'
        unique_together = (('eventid', 'donorid', 'donationno'),)


class Events(models.Model):
    eventid = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    event_name = models.CharField(max_length=30, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Log(models.Model):
    logid = models.BigIntegerField(primary_key=True)
    tablename = models.CharField(max_length=20, blank=True, null=True)
    operation = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Transaction(models.Model):
    transactionid = models.BigIntegerField(primary_key=True)
    donorid = models.ForeignKey(Donor, models.DO_NOTHING, db_column='donorid', blank=True, null=True)
    donationno = models.ForeignKey(Donation, models.DO_NOTHING, db_column='donationno', blank=True, null=True)
    date_paid = models.DateField(blank=True, null=True)
    time_paid = models.TimeField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction'
