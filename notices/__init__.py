from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.hashcompat import sha_constructor
import urllib, base64, re

def allowed_notice_types():
    if hasattr(settings, 'NOTICE_TYPES'):
        return settings.NOTICE_TYPES
    else:
        return ('success', 'notice', 'error')

def pack(str):
    return urllib.quote_plus(base64.b64encode("%s$%s" % (_hash(str), str)))

def unpack(str):
    decoded = urllib.unquote_plus(base64.b64decode(str))
    digest, plain = decoded.split("$", 1)
    if not digest or not plain or _hash(plain) != digest:
        raise ValueError, 'Malformed decoded notice'
    return plain

def _hash(str):
    if not hasattr(settings, 'SECRET_KEY') or not len(settings.SECRET_KEY):
        raise ValueError, 'SECRET_KEY needs to be defined in your settings.py'
    return sha_constructor(str + settings.SECRET_KEY).hexdigest()

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
