from notices import unpack, allowed_notice_types
import re

def notices(request):
    notices = {}
    for key, notice in request.GET.iteritems():
        type = re.sub('^_', '', key)
        if type in allowed_notice_types():
            notices[type] = unpack(notice)
    if len(notices) > 0:
        return { 'notices': notices }
    else:
        return {}
