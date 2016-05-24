import random
import string

from django import template

register = template.Library()


@register.simple_tag
def current_time(times):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(times))
