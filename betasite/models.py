# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Class(models.Model):
    classyear = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    coordinator = models.ForeignKey('Donor', models.DO_NOTHING, db_column='coordinator', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Donation(models.Model):
    donationno = models.AutoField(primary_key=True)
    donorid = models.ForeignKey('Donor', models.DO_NOTHING, db_column='donorid', blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    paymethod = models.CharField(max_length=-1, blank=True, null=True)
    installments = models.IntegerField(blank=True, null=True)
    pledge_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donation'


class Donor(models.Model):
    donorid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30, blank=True, null=True)
    mname = models.CharField(max_length=30, blank=True, null=True)
    lname = models.CharField(max_length=30, blank=True, null=True)
    contactno = models.CharField(max_length=12, blank=True, null=True)
    creditno = models.DecimalField(max_digits=16, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    donor_affiliation = models.ForeignKey('self', models.DO_NOTHING, db_column='donor_affiliation', blank=True, null=True)
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donor'


class EventDonation(models.Model):
    eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='eventid')
    donorid = models.ForeignKey(Donor, models.DO_NOTHING, db_column='donorid')
    donationno = models.ForeignKey(Donation, models.DO_NOTHING, db_column='donationno')

    class Meta:
        managed = False
        db_table = 'event_donation'
        unique_together = (('eventid', 'donorid', 'donationno'),)


class Events(models.Model):
    eventid = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=30, blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Transaction(models.Model):
    transactionid = models.AutoField(primary_key=True)
    donorid = models.ForeignKey(Donor, models.DO_NOTHING, db_column='donorid', blank=True, null=True)
    donationno = models.ForeignKey(Donation, models.DO_NOTHING, db_column='donationno', blank=True, null=True)
    date_paid = models.DateField(blank=True, null=True)
    time_paid = models.TimeField(blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction'
