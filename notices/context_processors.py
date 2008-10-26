from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.context_processors import PermWrapper
from notices import unpack, allowed_notice_types
import re

def notices(request):
    notices = {}
    try:
        for key, notice in request.GET.iteritems():
            type = re.sub('^_', '', key)
            if type in allowed_notice_types():
                notices[type] = unpack(notice)
        if len(notices) > 0:
            return { 'notices': notices }
        else:
            return {}
    except (ValueError, TypeError):
        return {}

def auth_without_messages(request):
    """
    A modified version of the bundled authentication context processor
    which does not retrieve per-user messages from the database.

    Be aware that the admin currently does not work when the default
    auth context processor is disabled when running in DEBUG mode.
    You will also loose feedback given with messages in the admin.
    """

    if settings.DEBUG and 'django.core.context_processors.auth' in settings.TEMPLATE_CONTEXT_PROCESSORS:
            raise ImproperlyConfigured("'django.core.context_processors.auth' can not be used together with 'notices.context_processors.auth_without_messages'")

    if hasattr(request, 'user'):
        user = request.user
    else:
        from django.contrib.auth.models import AnonymousUser
        user = AnonymousUser()
    return {
        'user': user,
        'messages': [],
        'perms': PermWrapper(user),
    }
