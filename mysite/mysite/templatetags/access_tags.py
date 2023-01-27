# access_tags.py

from django import template        

register = template.Library()

@register.filter
def last_message_dict(d, k):
    key = str(k['receiver__username']) +str(k['offer_id'])
    return d[key]

@register.filter
def key_dict(d, k):
    return d[k]