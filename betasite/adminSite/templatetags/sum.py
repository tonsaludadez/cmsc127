from django.db.models import Sum
from django import template

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