from django.http import HttpResponseRedirect
from django.conf import settings
import urllib, base64, re

def allowed_notice_types():
    if hasattr(settings, 'NOTICE_TYPES'):
        return settings.URLMESSAGE_TYPES
    else:
        return ('success', 'notice', 'error')

def pack(str):
    return urllib.quote_plus(base64.b64encode(str))

def unpack(str):
    return urllib.unquote_plus(base64.b64decode(str))

class HttpResponseRedirectWithNotice(HttpResponseRedirect):

    def __init__(self, redirect_to, **kwargs):
        self.url = redirect_to
        self.process_notices(kwargs)

        HttpResponseRedirect.__init__(self, self.url)

    def process_notices(self, notices):
        for type, notice in notices.iteritems():
            if type in allowed_notice_types():
                self.append_notice(type, notice)

    def append_notice(self, type, notice):
        if re.match("\?", self.url):
            self.url += "&_%s=%s" % (type, pack(notice))
        else:
            self.url += "?_%s=%s" % (type, pack(notice))
