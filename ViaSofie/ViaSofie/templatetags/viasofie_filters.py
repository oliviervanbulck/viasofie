# -*- coding: utf-8 -*-
from django import template
from django.contrib.auth.models import Group
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    """Returned of een user in een bepaalde groep zit"""
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter(name='euro')
def in_euro(waarde):
    """Returned een waarde met een euro teken in & met thousand-separators"""
    return mark_safe("&euro; %s" % (intcomma(int(waarde))))


@register.filter(name='opp')
def in_opp(waarde):
    """Returned een waarde met een m² er na"""
    return "%s m²" % waarde


@register.filter(name='ja_nee')
def in_ja_nee(waarde):
    """Returned Nee indien de gegeven waarde O is, anders is het Ja"""
    if waarde == 0:
        return 'Nee'
    else:
        return 'Ja'
