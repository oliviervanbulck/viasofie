# -*- coding: utf-8 -*-
from django import template
from django.contrib.auth.models import Group
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter(name='euro')
def in_euro(waarde):
    return mark_safe("&euro; %s" % (intcomma(int(waarde))))


@register.filter(name='opp')
def in_opp(waarde):
    return "%s m²" % waarde
