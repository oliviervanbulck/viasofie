import random
import string

from django import template

from panden.models import Switch

register = template.Library()


@register.simple_tag
def random_string(times):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(times))


@register.simple_tag
def pand_ref(pand):
    return pand.ref_number()


@register.assignment_tag()
def gebruik_zeshoeken():
    return Switch.objects.all().first().waarde


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
