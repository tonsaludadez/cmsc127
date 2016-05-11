from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Class(models.Model):
    classyear = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    coordinator = models.ForeignKey('Donor', models.DO_NOTHING, db_column='coordinator', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'

    def __str__(self):
    	return str(self.classyear)

class Donation(models.Model):
    donationno = models.AutoField(primary_key=True)
    donorid = models.ForeignKey('Donor', models.DO_NOTHING, db_column='donorid', blank=True, null=True, related_name='donations')
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    paymethod = models.CharField(max_length=1, blank=True, null=True)
    installments = models.IntegerField(blank=True, null=True)
    pledge_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donation'

    def __str__(self):
    	return str(self.donationno)

class Donor(models.Model):
    donorid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30, blank=True, null=True)
    mname = models.CharField(max_length=30, blank=True, null=True)
    lname = models.CharField(max_length=30, blank=True, null=True)
    contactno = models.CharField(max_length=12, blank=True, null=True)
    creditno = models.DecimalField(max_digits=16, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    donor_affiliation = models.ForeignKey('self', models.DO_NOTHING, db_column='donor_affiliation', blank=True, null=True)
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class', blank=True, null=True, related_name='donors')  # Field renamed because it was a Python reserved word.
    category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donor'

    def __str__(self):
    	return self.fname + " " + self.mname + " " + self.lname
        #return self.lname + ", " + self.fname + " " + self.mname


class EventDonation(models.Model):
    eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='eventid', related_name='eventDonation')
    donorid = models.ForeignKey(Donor, models.DO_NOTHING, db_column='donorid', related_name='events')
    donationno = models.ForeignKey(Donation, models.DO_NOTHING, db_column='donationno')

    class Meta:
        managed = False
        db_table = 'event_donation'
        unique_together = (('eventid', 'donorid', 'donationno'),)

    def __str__(self):
    	return str(self.eventid)


class Events(models.Model):
    eventid = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=30, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'

    def __str__(self):
    	return str(self.eventid)


class Transaction(models.Model):
    transactionid = models.AutoField(primary_key=True)
    donorid = models.ForeignKey(Donor, models.DO_NOTHING, db_column='donorid', blank=True, null=True, related_name='transactions')
    donationno = models.ForeignKey(Donation, models.DO_NOTHING, db_column='donationno', blank=True, null=True, related_name='transactions')
    date_paid = models.DateField(blank=True, null=True)
    time_paid = models.TimeField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction'

    def __str__(self):
    	return str(self.transactionid)

