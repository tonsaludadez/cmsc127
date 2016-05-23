from django.db.models import Sum
from django import template
import calendar

register = template.Library()

@register.filter(name='summation')
def summation(value):
	sum=0
	for item in value:
		sum = sum + item.amount_paid

	return sum

@register.filter(name='sub')
def sub(value, arg):
	return value-arg

@register.filter(name='totalpledges')
def total(value):
	sum = 0
	for item in value:
		sum = sum + item.donationno.amount

	return sum

@register.filter(name='totalgifts')
def totalGifts(value):
	sum = 0
	for item in value:
		for payment in item.donationno.transactions.all():
			sum = sum + payment.amount_paid

	return sum

@register.filter(name='totalGiftsDonation')
def totalGiftsDonation(value):
	sum = 0
	for item in value:
		for payment in item.transactions.all():
			sum = sum + payment.amount_paid
			
	return sum

@register.filter(name='month_name')
def month_name(month_number):
	return calendar.month_name[month_number]

@register.filter(name='get_percent')
def get_percent(num1, num2):
	return (num1/num2)*100
